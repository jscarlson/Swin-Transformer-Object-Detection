# the new config inherits the base configs to highlight the necessary modification
_base_ = './coco_instance.py'

# 1. dataset settings
dataset_type = 'CocoDataset'
classes = ('character', 'word',)
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_fewer/train80.json',
        img_prefix='/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_fewer/images'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_fewer/test20.json',
        img_prefix='/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_fewer/images'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_fewer/test20.json',
        img_prefix='/mnt/122a7683-fa4b-45dd-9f13-b18cc4f4a187/synthtxt_simpler_fewer/images'))
evaluation = dict(metric=['bbox', 'segm'], save_best='bbox_mAP_50')