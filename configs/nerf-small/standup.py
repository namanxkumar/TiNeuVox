_base_ = './default.py'

expname = 'small/dnerf_standup-400'
basedir = '/content/drive/My Drive/Colab Notebooks/TiNeuVox/logs/nerf_synthetic'

data = dict(
    datadir='/content/drive/My Drive/Colab Notebooks/TiNeuVox/data_dnerf/standup',
    dataset_type='dnerf',
    white_bkgd=True,
)
