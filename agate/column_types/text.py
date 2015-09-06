#!/usr/bin/env python

import six

from agate.column_types.base import *
from agate.exceptions import CastError

class TextType(ColumnType):
    """
    Column type for :class:`TextColumn`.
    """
    def test(self, d):
        """
        Test, for purposes of type inference, if a string value could possibly
        be valid for this column type.
        """
        return True

    def cast(self, d):
        """
        Cast a single value to :func:`unicode` (:func:`str` in Python 3).

        :param d: A value to cast.
        :returns: :func:`unicode` (:func:`str` in Python 3) or :code:`None`
        """
        if d is None:
            return d

        if isinstance(d, six.string_types):
            d = d.strip()

            if d.lower() in self.null_values:
                return None

        return six.text_type(d)

    def create_column(self, table, index):
        from agate.columns import TextColumn

        return TextColumn(table, index)
