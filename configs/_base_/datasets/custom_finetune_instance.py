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
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root+'train70-burlington-times-news-1989.json',
        img_prefix=data_root+'lines/'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root+'test30-burlington-times-news-1989.json',
        img_prefix=data_root+'lines/'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root+'test30-burlington-times-news-1989.json',
        img_prefix=data_root+'lines/'))