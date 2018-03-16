import json

from elementary import Annotations, AnnotationsType, Frame


def get_annotations_from_frames(frame_file):
    with open(frame_file, 'r') as f:
        frames_dict = json.load(f)

    annotations = Annotations(annotations_type=AnnotationsType.ground_truth)
    for frame_dict in frames_dict:
        annotations.add_frame(Frame.init_from_dict(frame_dict))

    return annotations


def save_frames_from_annotations_dict(ann_dict, frame_file):
    with open(frame_file, 'w') as f:
        json.dump(ann_dict['frames'], f, indent=2)
