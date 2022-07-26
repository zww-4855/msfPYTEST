"""
Unit and regression test for the msf_2022b package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import msf_2022b
import numpy as np

def test_calculate_angle():
    """ Test that calculate_angle function correctly determines the angle"""
    r1=np.array([0,0,-1])
    r2=np.array([0,0,0])
    r3=np.array([1,0,0])
    expected_angle=np.pi/2.0
    output_angle=msf_2022b.calculate_angle(r1,r2,r3)
    assert expected_angle==output_angle

def test_calculate_distance():
    """ Test that the calculate_distance function calculates what we expect"""
    r1=np.array([0,0,0])
    r2=np.array([0,1.0,0])

    expected_output=1.0
    observed_output=msf_2022b.calculate_distance(r1,r2)
    assert expected_output == observed_output

def test_msf_2022b_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "msf_2022b" in sys.modules
