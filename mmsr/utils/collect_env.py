from lmmcv.utils import collect_env as collect_base_env
from lmmcv.utils import get_git_hash

import mmsr


def collect_env():
    """Collect the information of the running environments."""
    env_info = collect_base_env()
    env_info['LMMSR'] = f'{mmsr.__version__}+{get_git_hash()[:7]}'

    return env_info


if __name__ == '__main__':
    for name, val in collect_env().items():
        print('{}: {}'.format(name, val))
