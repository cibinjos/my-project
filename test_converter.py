# test_converter.py — Unit tests for converter.py

import unittest
import converter


class TestTemperature(unittest.TestCase):

    # fahrenheit_to_celsius
    def test_f_to_c_freezing(self):
        self.assertAlmostEqual(converter.fahrenheit_to_celsius(32), 0.0, places=4)

    def test_f_to_c_boiling(self):
        self.assertAlmostEqual(converter.fahrenheit_to_celsius(212), 100.0, places=4)

    def test_f_to_c_intersection(self):
        self.assertAlmostEqual(converter.fahrenheit_to_celsius(-40), -40.0, places=4)

    # celsius_to_fahrenheit
    def test_c_to_f_freezing(self):
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(0), 32.0, places=4)

    def test_c_to_f_boiling(self):
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(100), 212.0, places=4)

    def test_c_to_f_intersection(self):
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(-40), -40.0, places=4)

    # fahrenheit_to_kelvin
    def test_f_to_k_freezing(self):
        self.assertAlmostEqual(converter.fahrenheit_to_kelvin(32), 273.15, places=4)

    def test_f_to_k_boiling(self):
        self.assertAlmostEqual(converter.fahrenheit_to_kelvin(212), 373.15, places=4)

    # kelvin_to_fahrenheit
    def test_k_to_f_freezing(self):
        self.assertAlmostEqual(converter.kelvin_to_fahrenheit(273.15), 32.0, places=4)

    def test_k_to_f_boiling(self):
        self.assertAlmostEqual(converter.kelvin_to_fahrenheit(373.15), 212.0, places=4)

    def test_k_to_f_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.kelvin_to_fahrenheit(-1)

    # celsius_to_kelvin
    def test_c_to_k_freezing(self):
        self.assertAlmostEqual(converter.celsius_to_kelvin(0), 273.15, places=4)

    def test_c_to_k_boiling(self):
        self.assertAlmostEqual(converter.celsius_to_kelvin(100), 373.15, places=4)

    # kelvin_to_celsius
    def test_k_to_c_freezing(self):
        self.assertAlmostEqual(converter.kelvin_to_celsius(273.15), 0.0, places=4)

    def test_k_to_c_absolute_zero(self):
        self.assertAlmostEqual(converter.kelvin_to_celsius(0), -273.15, places=4)

    def test_k_to_c_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.kelvin_to_celsius(-1)


class TestWeight(unittest.TestCase):

    # kg_to_lb
    def test_kg_to_lb_one(self):
        self.assertAlmostEqual(converter.kg_to_lb(1), 2.20462, places=4)

    def test_kg_to_lb_zero(self):
        self.assertAlmostEqual(converter.kg_to_lb(0), 0.0, places=4)

    def test_kg_to_lb_ten(self):
        self.assertAlmostEqual(converter.kg_to_lb(10), 22.0462, places=4)

    def test_kg_to_lb_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.kg_to_lb(-1)

    # lb_to_kg
    def test_lb_to_kg_one(self):
        self.assertAlmostEqual(converter.lb_to_kg(1), 0.4536, places=4)

    def test_lb_to_kg_zero(self):
        self.assertAlmostEqual(converter.lb_to_kg(0), 0.0, places=4)

    def test_lb_to_kg_ten(self):
        self.assertAlmostEqual(converter.lb_to_kg(10), 4.5359, places=4)

    def test_lb_to_kg_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.lb_to_kg(-5)


class TestLength(unittest.TestCase):

    # cm_to_feet
    def test_cm_to_feet_exact(self):
        self.assertAlmostEqual(converter.cm_to_feet(30.48), 1.0, places=4)

    def test_cm_to_feet_zero(self):
        self.assertAlmostEqual(converter.cm_to_feet(0), 0.0, places=4)

    def test_cm_to_feet_100(self):
        self.assertAlmostEqual(converter.cm_to_feet(100), 3.2808, places=4)

    def test_cm_to_feet_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.cm_to_feet(-10)

    # feet_to_cm
    def test_feet_to_cm_one(self):
        self.assertAlmostEqual(converter.feet_to_cm(1), 30.48, places=4)

    def test_feet_to_cm_zero(self):
        self.assertAlmostEqual(converter.feet_to_cm(0), 0.0, places=4)

    def test_feet_to_cm_five(self):
        self.assertAlmostEqual(converter.feet_to_cm(5), 152.4, places=4)

    def test_feet_to_cm_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.feet_to_cm(-1)

    # meters_to_yards
    def test_m_to_yd_one(self):
        self.assertAlmostEqual(converter.meters_to_yards(1), 1.09361, places=4)

    def test_m_to_yd_zero(self):
        self.assertAlmostEqual(converter.meters_to_yards(0), 0.0, places=4)

    def test_m_to_yd_100(self):
        self.assertAlmostEqual(converter.meters_to_yards(100), 109.361, places=4)

    def test_m_to_yd_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.meters_to_yards(-1)

    # yards_to_meters
    def test_yd_to_m_one(self):
        self.assertAlmostEqual(converter.yards_to_meters(1), 0.9144, places=4)

    def test_yd_to_m_zero(self):
        self.assertAlmostEqual(converter.yards_to_meters(0), 0.0, places=4)

    def test_yd_to_m_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.yards_to_meters(-3)


class TestSpeed(unittest.TestCase):

    # kmh_to_mph
    def test_kmh_to_mph_one(self):
        self.assertAlmostEqual(converter.kmh_to_mph(1), 0.621371, places=4)

    def test_kmh_to_mph_zero(self):
        self.assertAlmostEqual(converter.kmh_to_mph(0), 0.0, places=4)

    def test_kmh_to_mph_100(self):
        self.assertAlmostEqual(converter.kmh_to_mph(100), 62.1371, places=4)

    def test_kmh_to_mph_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.kmh_to_mph(-10)

    # mph_to_kmh
    def test_mph_to_kmh_one(self):
        self.assertAlmostEqual(converter.mph_to_kmh(1), 1.60934, places=4)

    def test_mph_to_kmh_zero(self):
        self.assertAlmostEqual(converter.mph_to_kmh(0), 0.0, places=4)

    def test_mph_to_kmh_60(self):
        self.assertAlmostEqual(converter.mph_to_kmh(60), 96.5607, places=4)

    def test_mph_to_kmh_negative_raises(self):
        with self.assertRaises(ValueError):
            converter.mph_to_kmh(-5)


if __name__ == "__main__":
    unittest.main()
