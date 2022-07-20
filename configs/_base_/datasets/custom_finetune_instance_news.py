# the new config inherits the base configs to highlight the necessary modification
_base_ = './coco_instance.py'

# 1. dataset settings
dataset_type = 'CocoDataset'
data_root = "/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/ocr_datasets/newspaper/"
classes = ('char', 'word',)
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'noisy_train70sofar_highres_expanded_comma_corrected.json',
        img_prefix=data_root + 'noisy_lines2/',
    ),
    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'noisy_val15sofar_highres_expanded_comma_corrected.json',
        img_prefix=data_root + 'noisy_lines2/',
    ),
    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'noisy_test15sofar_highres_expanded_comma_corrected.json',
        img_prefix=data_root + 'noisy_lines2/',
    ))
evaluation = dict(interval=1, metric='bbox', save_best='bbox_mAP', classwise=True)