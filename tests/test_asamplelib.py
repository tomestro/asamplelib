#!/usr/bin/env python

"""Tests for `asamplelib` package."""

import pytest


from asamplelib import asamplelib


@pytest.fixture
def sample_fixture():
    """Setup test fixture"""
    return 1


def test_func(sample_fixture):
    """Test the sample function"""
    assert asamplelib.sample_func(1) == 2


def test_negative(sample_fixture):
    """Negative test of sample function"""
    assert asamplelib.sample_func(-2) == -1


def test_inc():
    assert asamplelib.inc(1) == 2


def test_dec():
    assert asamplelib.dec(2) == 2

def test_sum():
    assert asamplelib.sum(3, 4) == 7


def test_mult():
    assert asamplelib.mult(3, 4) == 12


def test_square():
    assert asamplelib.square(5) == 25
