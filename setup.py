from setuptools import setup, find_packages

from SPVec import __version__

setup(name='SPVec',
      version=__version__,
      description='SPVec - an unsupervised representation learning method to learn vector representations of molecular substructures and protein sequences ',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD 3-clause',
        'Programming Language :: Python :: 3.6',
        'Topic :: Bioinformatics :: Featurization',
      ],
      url='https://github.com/dqwei-lab/SPVec',
      author='Yufang Zhang, Xiangeng Wang, Yanyi Chu, et al.',
      author_email='yufangz@sjtu.edu.cn,wangxiangeng @sjtu.edu.cn, a96123155@sjtu.edu.cn',
      license='BSD 3-clause',
      packages=find_packages(),
      install_requires=['numpy', 'gensim', 'tqdm', 'joblib', 'pandas', 'matplotlib', 'IPython', 'seaborn','jieba',],
      zip_safe=False,
      entry_points="""
      [console_scripts]
      """
      )
