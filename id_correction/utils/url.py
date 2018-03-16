import boto3

from .s3 import parse_s3_path


# TODO: Document
def get_signed_s3_url(s3_path, expiry_seconds=3600):
    r"""
    Generates a signed S3 url for the S3File.
    This is necessary for exposing S3 file URLs publicly.

    Parameters
    ----------
    expiry_seconds : int, optional
        Number of seconds until the signed URL should expire.

    Returns
    -------
    signed_url : str
        The signed S3 url.
    """

    s3_bucket, s3_key = parse_s3_path(s3_path)
    return boto3.client('s3', 'us-east-1').generate_presigned_url(
        'get_object',
        Params={'Bucket': s3_bucket, 'Key': s3_key},
        ExpiresIn=expiry_seconds).replace('https://', 'http://', 1)
