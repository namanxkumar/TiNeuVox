_base_ = './default.py'

expname = 'small/dnerf_standup-400'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/content/drive/My Drive/Colab Notebooks/data_dnerf/standup',
    dataset_type='dnerf',
    white_bkgd=True,
)
