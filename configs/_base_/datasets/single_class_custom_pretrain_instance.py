# the new config inherits the base configs to highlight the necessary modification
_base_ = './coco_instance.py'

# 1. dataset settings
dataset_type = 'CocoDataset'
data_root = '/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_more/'
classes = ('character',)
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root+'train90.json',
        img_prefix=data_root+'images/'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root+'test10.json',
        img_prefix=data_root+'images/'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root+'test10.json',
        img_prefix=data_root+'images/'))
evaluation = dict(metric=['bbox', 'segm'], save_best='bbox_mAP', classwise=True)