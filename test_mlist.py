import mlist
import mock


def write():
    with mock.patch.object(__builtins__, 'input', lambda: '12'):
        assert mlist.capacity == 12


write()
