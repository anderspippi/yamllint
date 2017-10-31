# -*- coding: utf-8 -*-
# Copyright (C) 2017 Greg Dubicki
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Use this rule to prevent nodes with empty content, that implicitly result in
``null`` values.

.. rubric:: Options

* Use ``forbid-in-block-mappings`` to prevent implicit empty values in block
  mappings.

.. rubric:: Examples

#. With ``empty-values: {forbid-in-block-mappings: true}``
   the following code snippets would **PASS**:
   ::

    some-mapping:
      sub-element: correctly indented

   ::

    explicitly-null: null

   the following code snippets would **FAIL**:
   ::

    some-mapping:
    sub-element: incorrectly indented

   ::

    implicitly-null:

"""

import yaml

from yamllint.linter import LintProblem


ID = 'empty-values'
TYPE = 'token'
CONF = {'forbid-in-block-mappings': bool}


def check(conf, token, prev, next, nextnext, context):

    if conf['forbid-in-block-mappings']:
        if isinstance(token, yaml.ValueToken) and isinstance(next, (
                yaml.KeyToken, yaml.BlockEndToken,
                yaml.StreamEndToken, yaml.DocumentEndToken)):
            yield LintProblem(token.start_mark.line + 1,
                              token.end_mark.column + 1,
                              'empty value in block mapping')