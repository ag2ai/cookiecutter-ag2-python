# Copyright (c) 2023 - 2025, AG2ai, Inc., AG2ai open-source projects maintainers and core contributors
#
# SPDX-License-Identifier: Apache-2.0

import {{cookiecutter.project_slug}}


def test_version() -> None:
    assert {{cookiecutter.project_slug}}.__version__ is not None
