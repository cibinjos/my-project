# converter.py — All unit conversion functions

# ── Constants ──────────────────────────────────────────────────────────────
KG_TO_LB        = 2.20462
CM_PER_FOOT     = 30.48
M_TO_YARD       = 1.09361
KMH_TO_MPH      = 0.621371
CELSIUS_OFFSET  = 273.15   # offset between Celsius and Kelvin


# ── Temperature ────────────────────────────────────────────────────────────

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius: °C = (°F - 32) × 5/9"""
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit: °F = (°C × 9/5) + 32"""
    return (c * 9 / 5) + 32


def fahrenheit_to_kelvin(f: float) -> float:
    """Convert Fahrenheit to Kelvin: K = (°F - 32) × 5/9 + 273.15"""
    return fahrenheit_to_celsius(f) + CELSIUS_OFFSET


def kelvin_to_fahrenheit(k: float) -> float:
    """Convert Kelvin to Fahrenheit: °F = (K - 273.15) × 9/5 + 32"""
    if k < 0:
        raise ValueError(f"Kelvin cannot be negative (got {k})")
    return celsius_to_fahrenheit(k - CELSIUS_OFFSET)


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin: K = °C + 273.15"""
    return c + CELSIUS_OFFSET


def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius: °C = K - 273.15"""
    if k < 0:
        raise ValueError(f"Kelvin cannot be negative (got {k})")
    return k - CELSIUS_OFFSET


# ── Weight ─────────────────────────────────────────────────────────────────

def kg_to_lb(kg: float) -> float:
    """Convert kilograms to pounds: lb = kg × 2.20462"""
    if kg < 0:
        raise ValueError(f"Weight cannot be negative (got {kg})")
    return kg * KG_TO_LB


def lb_to_kg(lb: float) -> float:
    """Convert pounds to kilograms: kg = lb / 2.20462"""
    if lb < 0:
        raise ValueError(f"Weight cannot be negative (got {lb})")
    return lb / KG_TO_LB


# ── Length ─────────────────────────────────────────────────────────────────

def cm_to_feet(cm: float) -> float:
    """Convert centimeters to feet: ft = cm / 30.48"""
    if cm < 0:
        raise ValueError(f"Length cannot be negative (got {cm})")
    return cm / CM_PER_FOOT


def feet_to_cm(ft: float) -> float:
    """Convert feet to centimeters: cm = ft × 30.48"""
    if ft < 0:
        raise ValueError(f"Length cannot be negative (got {ft})")
    return ft * CM_PER_FOOT


def meters_to_yards(m: float) -> float:
    """Convert meters to yards: yd = m × 1.09361"""
    if m < 0:
        raise ValueError(f"Length cannot be negative (got {m})")
    return m * M_TO_YARD


def yards_to_meters(yd: float) -> float:
    """Convert yards to meters: m = yd / 1.09361"""
    if yd < 0:
        raise ValueError(f"Length cannot be negative (got {yd})")
    return yd / M_TO_YARD


# ── Speed ──────────────────────────────────────────────────────────────────

def kmh_to_mph(kmh: float) -> float:
    """Convert km/h to mph: mph = km/h × 0.621371"""
    if kmh < 0:
        raise ValueError(f"Speed cannot be negative (got {kmh})")
    return kmh * KMH_TO_MPH


def mph_to_kmh(mph: float) -> float:
    """Convert mph to km/h: km/h = mph / 0.621371"""
    if mph < 0:
        raise ValueError(f"Speed cannot be negative (got {mph})")
    return mph / KMH_TO_MPH
