# Task: Python Unit Converter Calculator

## Overview
Build a command-line Python calculator that converts between common units across temperature, weight, length, and speed categories.

---

## Supported Conversions

| Category    | Conversions |
|-------------|-------------|
| Temperature | Fahrenheit ↔ Celsius, Fahrenheit ↔ Kelvin, Celsius ↔ Kelvin |
| Weight      | Kilograms ↔ Pounds |
| Length      | Centimeters ↔ Feet, Meters ↔ Yards |
| Speed       | km/h ↔ mph |

---

## Tasks

### Task 1 — Project Structure
- [ ] Create `converter.py` — contains all conversion functions
- [ ] Create `main.py` — interactive CLI menu
- [ ] Create `test_converter.py` — unit tests

**File layout:**
```
my-project/
├── converter.py
├── main.py
├── test_converter.py
└── task.md
```

---

### Task 2 — Temperature Conversions (`converter.py`)

Implement the following functions:

#### 2.1 Fahrenheit → Celsius
```
°C = (°F - 32) × 5/9
```
```python
def fahrenheit_to_celsius(f: float) -> float
```

#### 2.2 Celsius → Fahrenheit
```
°F = (°C × 9/5) + 32
```
```python
def celsius_to_fahrenheit(c: float) -> float
```

#### 2.3 Fahrenheit → Kelvin
```
K = (°F - 32) × 5/9 + 273.15
```
```python
def fahrenheit_to_kelvin(f: float) -> float
```

#### 2.4 Kelvin → Fahrenheit
```
°F = (K - 273.15) × 9/5 + 32
```
```python
def kelvin_to_fahrenheit(k: float) -> float
```

#### 2.5 Celsius → Kelvin
```
K = °C + 273.15
```
```python
def celsius_to_kelvin(c: float) -> float
```

#### 2.6 Kelvin → Celsius
```
°C = K - 273.15
```
```python
def kelvin_to_celsius(k: float) -> float
```

**Constraint:** Raise `ValueError` if Kelvin input is below 0 (absolute zero).

---

### Task 3 — Weight Conversions (`converter.py`)

#### 3.1 Kilograms → Pounds
```
lb = kg × 2.20462
```
```python
def kg_to_lb(kg: float) -> float
```

#### 3.2 Pounds → Kilograms
```
kg = lb / 2.20462
```
```python
def lb_to_kg(lb: float) -> float
```

**Constraint:** Raise `ValueError` if input is negative.

---

### Task 4 — Length Conversions (`converter.py`)

#### 4.1 Centimeters → Feet
```
ft = cm / 30.48
```
```python
def cm_to_feet(cm: float) -> float
```

#### 4.2 Feet → Centimeters
```
cm = ft × 30.48
```
```python
def feet_to_cm(ft: float) -> float
```

#### 4.3 Meters → Yards
```
yd = m × 1.09361
```
```python
def meters_to_yards(m: float) -> float
```

#### 4.4 Yards → Meters
```
m = yd / 1.09361
```
```python
def yards_to_meters(yd: float) -> float
```

**Constraint:** Raise `ValueError` if input is negative.

---

### Task 5 — Speed Conversions (`converter.py`)

#### 5.1 km/h → mph
```
mph = km/h × 0.621371
```
```python
def kmh_to_mph(kmh: float) -> float
```

#### 5.2 mph → km/h
```
km/h = mph / 0.621371
```
```python
def mph_to_kmh(mph: float) -> float
```

**Constraint:** Raise `ValueError` if input is negative.

---

### Task 6 — CLI Interface (`main.py`)

- [ ] Display a categorized menu on launch
- [ ] Prompt user to select a conversion category, then a specific conversion
- [ ] Accept numeric input from the user
- [ ] Display the result rounded to 4 decimal places with units
- [ ] Allow the user to perform another conversion or quit
- [ ] Handle invalid input gracefully (non-numeric, out-of-range) with a clear error message — do not crash

**Example interaction:**
```
=== Unit Converter ===
1. Temperature
2. Weight
3. Length
4. Speed
0. Quit

Select category: 1

--- Temperature ---
1. Fahrenheit → Celsius
2. Celsius → Fahrenheit
3. Fahrenheit → Kelvin
4. Kelvin → Fahrenheit
5. Celsius → Kelvin
6. Kelvin → Celsius

Select conversion: 1
Enter value in Fahrenheit: 212

Result: 212.0 °F = 100.0 °C
```

---

### Task 7 — Tests (`test_converter.py`)

Use Python's built-in `unittest` module. All tests must use `assertAlmostEqual` with `places=4` for floating-point comparisons.

---

## Test Cases

### Temperature Tests

| Function                  | Input       | Expected Output | Notes               |
|---------------------------|-------------|-----------------|---------------------|
| `fahrenheit_to_celsius`   | 32          | 0.0             | Freezing point      |
| `fahrenheit_to_celsius`   | 212         | 100.0           | Boiling point       |
| `fahrenheit_to_celsius`   | -40         | -40.0           | F and C intersect   |
| `celsius_to_fahrenheit`   | 0           | 32.0            | Freezing point      |
| `celsius_to_fahrenheit`   | 100         | 212.0           | Boiling point       |
| `celsius_to_fahrenheit`   | -40         | -40.0           | F and C intersect   |
| `fahrenheit_to_kelvin`    | 32          | 273.15          | Freezing point      |
| `fahrenheit_to_kelvin`    | 212         | 373.15          | Boiling point       |
| `kelvin_to_fahrenheit`    | 273.15      | 32.0            | Freezing point      |
| `kelvin_to_fahrenheit`    | 373.15      | 212.0           | Boiling point       |
| `celsius_to_kelvin`       | 0           | 273.15          | Freezing point      |
| `celsius_to_kelvin`       | 100         | 373.15          | Boiling point       |
| `kelvin_to_celsius`       | 273.15      | 0.0             | Freezing point      |
| `kelvin_to_celsius`       | 0           | -273.15         | Absolute zero       |
| `kelvin_to_fahrenheit`    | -1          | raises ValueError | Below absolute zero |
| `kelvin_to_celsius`       | -1          | raises ValueError | Below absolute zero |

### Weight Tests

| Function    | Input  | Expected Output | Notes            |
|-------------|--------|-----------------|------------------|
| `kg_to_lb`  | 1      | 2.20462         | 1 kg baseline    |
| `kg_to_lb`  | 0      | 0.0             | Zero             |
| `kg_to_lb`  | 10     | 22.0462         |                  |
| `lb_to_kg`  | 1      | 0.4536          | 1 lb baseline    |
| `lb_to_kg`  | 0      | 0.0             | Zero             |
| `lb_to_kg`  | 10     | 4.5359          |                  |
| `kg_to_lb`  | -1     | raises ValueError | Negative input |
| `lb_to_kg`  | -5     | raises ValueError | Negative input |

### Length Tests

| Function          | Input  | Expected Output | Notes              |
|-------------------|--------|-----------------|--------------------|
| `cm_to_feet`      | 30.48  | 1.0             | Exact 1 foot       |
| `cm_to_feet`      | 0      | 0.0             | Zero               |
| `cm_to_feet`      | 100    | 3.2808          |                    |
| `feet_to_cm`      | 1      | 30.48           | Exact 1 foot       |
| `feet_to_cm`      | 0      | 0.0             | Zero               |
| `feet_to_cm`      | 5      | 152.4           |                    |
| `meters_to_yards` | 1      | 1.09361         | 1 m baseline       |
| `meters_to_yards` | 0      | 0.0             | Zero               |
| `meters_to_yards` | 100    | 109.361         |                    |
| `yards_to_meters` | 1      | 0.9144          | 1 yd baseline      |
| `yards_to_meters` | 0      | 0.0             | Zero               |
| `cm_to_feet`      | -10    | raises ValueError | Negative input   |
| `meters_to_yards` | -1     | raises ValueError | Negative input   |

### Speed Tests

| Function      | Input  | Expected Output | Notes              |
|---------------|--------|-----------------|--------------------|
| `kmh_to_mph`  | 1      | 0.62137         | 1 km/h baseline    |
| `kmh_to_mph`  | 0      | 0.0             | Zero               |
| `kmh_to_mph`  | 100    | 62.1371         | Highway speed      |
| `mph_to_kmh`  | 1      | 1.60934         | 1 mph baseline     |
| `mph_to_kmh`  | 0      | 0.0             | Zero               |
| `mph_to_kmh`  | 60     | 96.5606         | Highway speed      |
| `kmh_to_mph`  | -10    | raises ValueError | Negative input   |
| `mph_to_kmh`  | -5     | raises ValueError | Negative input   |

---

## Passing Criteria

### Functional Correctness
- [ ] All 14 conversion functions exist and are importable from `converter.py`
- [ ] All test cases in the table above pass with `assertAlmostEqual(places=4)`
- [ ] `ValueError` is raised (not silently ignored) for all invalid inputs listed above

### Code Quality
- [ ] No conversion logic lives in `main.py` — only in `converter.py`
- [ ] No magic numbers inline in functions — use named constants or clear formulas with comments
- [ ] Each function accepts a `float` and returns a `float`

### CLI Behavior
- [ ] Menu displays all categories and options correctly
- [ ] Invalid menu selections print an error and re-prompt (no crash)
- [ ] Non-numeric input prints an error and re-prompt (no crash)
- [ ] Results display the input value, unit, converted value, and unit
- [ ] User can run multiple conversions in one session

### Tests
- [ ] `python -m unittest test_converter.py` runs with **0 failures, 0 errors**
- [ ] Test file covers every function with at least 2 valid inputs and 1 invalid input
- [ ] Tests are grouped by category using `TestCase` subclasses

---

## How to Run

```bash
# Run the calculator
python main.py

# Run all tests
python -m unittest test_converter.py -v
```
