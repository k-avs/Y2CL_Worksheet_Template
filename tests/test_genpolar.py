from importlib import import_module
from collections.abc import Generator
from inspect import signature
import numpy as np
import pytest

@pytest.fixture(scope="module")
def genpolar():
    return import_module("src.genpolar")


class TestTask12:

    def test_genpolar_exists(self, genpolar):
        pass

    def test_rtrings_exists(self, genpolar):
        assert hasattr(genpolar, "rtrings")

    def test_rtrings_args(self, genpolar):
        assert not {'nrings', 'rmax', 'multi'}.difference(signature(genpolar.rtrings).parameters.keys())

    def test_generator_type(self, genpolar):
        assert isinstance(genpolar.rtrings(rmax=5., nrings=5, multi=6), Generator)

    def test_rtrings_correct(self, genpolar):
        assert np.allclose(list(genpolar.rtrings(rmax=5., nrings=5, multi=6)),
                           [(0.0, 0.0),
                            (1.0, 0.0),
                            (1.0, 1.0471975511965976),
                            (1.0, 2.0943951023931953),
                            (1.0, 3.141592653589793),
                            (1.0, 4.1887902047863905),
                            (1.0, 5.235987755982988),
                            (2.0, 0.0),
                            (2.0, 0.5235987755982988),
                            (2.0, 1.0471975511965976),
                            (2.0, 1.5707963267948966),
                            (2.0, 2.0943951023931953),
                            (2.0, 2.617993877991494),
                            (2.0, 3.141592653589793),
                            (2.0, 3.665191429188092),
                            (2.0, 4.1887902047863905),
                            (2.0, 4.71238898038469),
                            (2.0, 5.235987755982988),
                            (2.0, 5.759586531581287),
                            (3.0, 0.0),
                            (3.0, 0.3490658503988659),
                            (3.0, 0.6981317007977318),
                            (3.0, 1.0471975511965976),
                            (3.0, 1.3962634015954636),
                            (3.0, 1.7453292519943295),
                            (3.0, 2.0943951023931953),
                            (3.0, 2.443460952792061),
                            (3.0, 2.792526803190927),
                            (3.0, 3.141592653589793),
                            (3.0, 3.490658503988659),
                            (3.0, 3.839724354387525),
                            (3.0, 4.1887902047863905),
                            (3.0, 4.537856055185257),
                            (3.0, 4.886921905584122),
                            (3.0, 5.235987755982989),
                            (3.0, 5.585053606381854),
                            (3.0, 5.93411945678072),
                            (4.0, 0.0),
                            (4.0, 0.2617993877991494),
                            (4.0, 0.5235987755982988),
                            (4.0, 0.7853981633974483),
                            (4.0, 1.0471975511965976),
                            (4.0, 1.308996938995747),
                            (4.0, 1.5707963267948966),
                            (4.0, 1.832595714594046),
                            (4.0, 2.0943951023931953),
                            (4.0, 2.356194490192345),
                            (4.0, 2.617993877991494),
                            (4.0, 2.8797932657906435),
                            (4.0, 3.141592653589793),
                            (4.0, 3.4033920413889422),
                            (4.0, 3.665191429188092),
                            (4.0, 3.926990816987241),
                            (4.0, 4.1887902047863905),
                            (4.0, 4.45058959258554),
                            (4.0, 4.71238898038469),
                            (4.0, 4.974188368183839),
                            (4.0, 5.235987755982988),
                            (4.0, 5.497787143782138),
                            (4.0, 5.759586531581287),
                            (4.0, 6.021385919380436),
                            (5.0, 0.0),
                            (5.0, 0.20943951023931953),
                            (5.0, 0.41887902047863906),
                            (5.0, 0.6283185307179586),
                            (5.0, 0.8377580409572781),
                            (5.0, 1.0471975511965976),
                            (5.0, 1.2566370614359172),
                            (5.0, 1.4660765716752366),
                            (5.0, 1.6755160819145563),
                            (5.0, 1.8849555921538759),
                            (5.0, 2.0943951023931953),
                            (5.0, 2.3038346126325147),
                            (5.0, 2.5132741228718345),
                            (5.0, 2.722713633111154),
                            (5.0, 2.9321531433504733),
                            (5.0, 3.141592653589793),
                            (5.0, 3.3510321638291125),
                            (5.0, 3.560471674068432),
                            (5.0, 3.7699111843077517),
                            (5.0, 3.979350694547071),
                            (5.0, 4.1887902047863905),
                            (5.0, 4.39822971502571),
                            (5.0, 4.607669225265029),
                            (5.0, 4.817108735504349),
                            (5.0, 5.026548245743669),
                            (5.0, 5.235987755982988),
                            (5.0, 5.445427266222308),
                            (5.0, 5.654866776461628),
                            (5.0, 5.864306286700947),
                            (5.0, 6.073745796940266)])
