# -*- coding: utf-8 -*-
#
# Copyright 2015 Yuriy Gavenchuk aka murminathor
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import TestCase, mock
from web_deploy.project import ProjectModule


__author__ = 'y.gavenchuk'
__all__ = ('ProjectModuleTestCase', )


class ProjectModuleTestCase(TestCase):
    def test_setup_path(self):
        path_before = '/a/b/c'
        path_after = '/e/f/g'
        git = mock.MagicMock()

        pm = ProjectModule(path_before, git)
        pm.path = path_after

        self.assertEqual(pm.path, "%s/%s" % (path_after, pm.container))
