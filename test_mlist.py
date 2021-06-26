import mlist
import mock
import pytest

def write():
    with mock.patch.object(__builtins__, 'input', lambda: '12'):
        assert mlist.capacity == 12

write()