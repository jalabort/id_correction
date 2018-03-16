import re

s3_path_regex = re.compile('s3://([^/]*)/(.*)')


def parse_s3_url(url):
    r"""
    Parse S3 Url into parts.

    Parameters
    ----------
    url : basestring
        Url to be broken up

    Returns
    -------
    bucket_name : str
    region : str
    key : str
    """
    bucket_name = None
    region = None
    key = None

    # http://bucket.s3.amazonaws.com/key1/key2
    match = re.search('^https?://([^.]+).s3.amazonaws.com(.*?)$', url)
    if match:
        # No region specified means us-east-1
        bucket_name, region, key = match.group(1), 'us-east-1', match.group(2)

    # http://bucket.s3-aws-region.amazonaws.com/key1/key2
    match = re.search('^https?://([^.]+).s3-([^.]+).amazonaws.com(.*?)$', url)
    if match:
        bucket_name, region, key = (
            match.group(1), match.group(2), match.group(3))

    # http://s3.amazonaws.com/bucket/key1/key2
    match = re.search('^https?://s3.amazonaws.com/([^/]+)(.*?)$', url)
    if match:
        # No region specified means us-east-1
        bucket_name, region, key = match.group(1), 'us-east-1', match.group(2)

    # http://s3-aws-region.amazonaws.com/bucket/key1/key2
    match = re.search('^https?://s3-([^.]+).amazonaws.com/([^/]+)(.*?)$',
                      url)
    if match:
        bucket_name, region, key = (
            match.group(2), match.group(1), match.group(3))

    # http://s3.aws-region.amazonaws.com/bucket/key1/key2
    match = re.search('^https?://s3.([^.]+).amazonaws.com/([^/]+)(.*?)$', url)
    if match:
        bucket_name, region, key = (
            match.group(2), match.group(1), match.group(3))

    pieces = [bucket_name, region, key]
    if any(map(lambda p: p is None, pieces)):
        raise Exception("Error parsing S3 URL: "
                        "bucket: {}, region: {}, key: {}".format(
                            bucket_name, region, key))

    return list(map(lambda x: x.strip('/'), pieces))


def parse_s3_path(path):
    """
    Parses an s3 path of the form s3://<bucket>/<key> into bucket and
    key. Returns (None, None) if input path is not in the correct form.

    Parameters
    ----------
    path : str
        The s3 path to parse

    Returns
    -------
    bucket, key : tuple(str, str)
        The parsed bucket and key.
    """
    match = s3_path_regex.match(path)

    if match is None:
        return None, None

    groups = match.groups()
    return groups[0], groups[1]
