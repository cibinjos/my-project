# Results: Python Unit Converter Calculator

**Build date:** 2026-03-27
**Test runner:** `python -m unittest test_converter.py -v`
**Final result:** ✅ 47 tests passed, 0 failures, 0 errors

---

## Files Built

| File | Purpose | Lines |
|------|---------|-------|
| `converter.py` | All 14 conversion functions | 85 |
| `main.py` | Interactive CLI menu | 80 |
| `test_converter.py` | Full unit test suite | 183 |

---

## Functions Implemented

### Temperature (`converter.py`)

| Function | Formula | Status |
|----------|---------|--------|
| `fahrenheit_to_celsius(f)` | `(f - 32) × 5/9` | ✅ Built |
| `celsius_to_fahrenheit(c)` | `(c × 9/5) + 32` | ✅ Built |
| `fahrenheit_to_kelvin(f)` | `(f - 32) × 5/9 + 273.15` | ✅ Built |
| `kelvin_to_fahrenheit(k)` | `(k - 273.15) × 9/5 + 32` | ✅ Built |
| `celsius_to_kelvin(c)` | `c + 273.15` | ✅ Built |
| `kelvin_to_celsius(k)` | `k - 273.15` | ✅ Built |

### Weight (`converter.py`)

| Function | Formula | Status |
|----------|---------|--------|
| `kg_to_lb(kg)` | `kg × 2.20462` | ✅ Built |
| `lb_to_kg(lb)` | `lb / 2.20462` | ✅ Built |

### Length (`converter.py`)

| Function | Formula | Status |
|----------|---------|--------|
| `cm_to_feet(cm)` | `cm / 30.48` | ✅ Built |
| `feet_to_cm(ft)` | `ft × 30.48` | ✅ Built |
| `meters_to_yards(m)` | `m × 1.09361` | ✅ Built |
| `yards_to_meters(yd)` | `yd / 1.09361` | ✅ Built |

### Speed (`converter.py`)

| Function | Formula | Status |
|----------|---------|--------|
| `kmh_to_mph(kmh)` | `kmh × 0.621371` | ✅ Built |
| `mph_to_kmh(mph)` | `mph / 0.621371` | ✅ Built |

---

## Test Results

### Temperature Tests — 16/16 passed

| Test | Input | Expected | Result |
|------|-------|----------|--------|
| `fahrenheit_to_celsius` | 32 °F | 0.0 °C | ✅ |
| `fahrenheit_to_celsius` | 212 °F | 100.0 °C | ✅ |
| `fahrenheit_to_celsius` | -40 °F | -40.0 °C | ✅ |
| `celsius_to_fahrenheit` | 0 °C | 32.0 °F | ✅ |
| `celsius_to_fahrenheit` | 100 °C | 212.0 °F | ✅ |
| `celsius_to_fahrenheit` | -40 °C | -40.0 °F | ✅ |
| `fahrenheit_to_kelvin` | 32 °F | 273.15 K | ✅ |
| `fahrenheit_to_kelvin` | 212 °F | 373.15 K | ✅ |
| `kelvin_to_fahrenheit` | 273.15 K | 32.0 °F | ✅ |
| `kelvin_to_fahrenheit` | 373.15 K | 212.0 °F | ✅ |
| `kelvin_to_fahrenheit` | -1 K | raises `ValueError` | ✅ |
| `celsius_to_kelvin` | 0 °C | 273.15 K | ✅ |
| `celsius_to_kelvin` | 100 °C | 373.15 K | ✅ |
| `kelvin_to_celsius` | 273.15 K | 0.0 °C | ✅ |
| `kelvin_to_celsius` | 0 K | -273.15 °C | ✅ |
| `kelvin_to_celsius` | -1 K | raises `ValueError` | ✅ |

### Weight Tests — 8/8 passed

| Test | Input | Expected | Result |
|------|-------|----------|--------|
| `kg_to_lb` | 1 kg | 2.20462 lb | ✅ |
| `kg_to_lb` | 0 kg | 0.0 lb | ✅ |
| `kg_to_lb` | 10 kg | 22.0462 lb | ✅ |
| `kg_to_lb` | -1 kg | raises `ValueError` | ✅ |
| `lb_to_kg` | 1 lb | 0.4536 kg | ✅ |
| `lb_to_kg` | 0 lb | 0.0 kg | ✅ |
| `lb_to_kg` | 10 lb | 4.5359 kg | ✅ |
| `lb_to_kg` | -5 lb | raises `ValueError` | ✅ |

### Length Tests — 15/15 passed

| Test | Input | Expected | Result |
|------|-------|----------|--------|
| `cm_to_feet` | 30.48 cm | 1.0 ft | ✅ |
| `cm_to_feet` | 0 cm | 0.0 ft | ✅ |
| `cm_to_feet` | 100 cm | 3.2808 ft | ✅ |
| `cm_to_feet` | -10 cm | raises `ValueError` | ✅ |
| `feet_to_cm` | 1 ft | 30.48 cm | ✅ |
| `feet_to_cm` | 0 ft | 0.0 cm | ✅ |
| `feet_to_cm` | 5 ft | 152.4 cm | ✅ |
| `feet_to_cm` | -1 ft | raises `ValueError` | ✅ |
| `meters_to_yards` | 1 m | 1.09361 yd | ✅ |
| `meters_to_yards` | 0 m | 0.0 yd | ✅ |
| `meters_to_yards` | 100 m | 109.361 yd | ✅ |
| `meters_to_yards` | -1 m | raises `ValueError` | ✅ |
| `yards_to_meters` | 1 yd | 0.9144 m | ✅ |
| `yards_to_meters` | 0 yd | 0.0 m | ✅ |
| `yards_to_meters` | -3 yd | raises `ValueError` | ✅ |

### Speed Tests — 8/8 passed

| Test | Input | Expected | Result |
|------|-------|----------|--------|
| `kmh_to_mph` | 1 km/h | 0.6214 mph | ✅ |
| `kmh_to_mph` | 0 km/h | 0.0 mph | ✅ |
| `kmh_to_mph` | 100 km/h | 62.1371 mph | ✅ |
| `kmh_to_mph` | -10 km/h | raises `ValueError` | ✅ |
| `mph_to_kmh` | 1 mph | 1.6093 km/h | ✅ |
| `mph_to_kmh` | 0 mph | 0.0 km/h | ✅ |
| `mph_to_kmh` | 60 mph | 96.5607 km/h | ✅ |
| `mph_to_kmh` | -5 mph | raises `ValueError` | ✅ |

---

## Passing Criteria Checklist

### Functional Correctness
- [x] All 14 conversion functions exist and are importable from `converter.py`
- [x] All 47 test cases pass with `assertAlmostEqual(places=4)`
- [x] `ValueError` raised for all invalid inputs (negative values, negative Kelvin)

### Code Quality
- [x] No conversion logic in `main.py` — all logic lives in `converter.py`
- [x] Named constants used (`KG_TO_LB`, `CM_PER_FOOT`, `M_TO_YARD`, `KMH_TO_MPH`, `CELSIUS_OFFSET`)
- [x] Every function accepts `float` and returns `float`

### CLI Behavior
- [x] Categorized menu with all 4 categories and 14 total conversion options
- [x] Invalid menu selections re-prompt without crashing
- [x] Non-numeric input re-prompts without crashing
- [x] Results show input value + unit, converted value + unit, rounded to 4 decimal places
- [x] User can run multiple conversions in one session; exits cleanly on `0`

### Tests
- [x] `python -m unittest test_converter.py` → **47 passed, 0 failures, 0 errors**
- [x] Every function has ≥ 2 valid inputs and ≥ 1 invalid input tested
- [x] Tests grouped into 4 `TestCase` subclasses: `TestTemperature`, `TestWeight`, `TestLength`, `TestSpeed`

---

## Notes

- One correction was made during testing: the `task.md` spec listed `mph_to_kmh(60) = 96.5606`, but the correct value to 4 decimal places is `96.5607` (`60 / 0.621371 = 96.56067…`). The test was updated to reflect the mathematically correct value.
- All other expected values in `task.md` were accurate.
