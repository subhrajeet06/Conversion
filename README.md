# 🚀 Conversion - Python Package for Unit Conversion

**Conversion** is a modular Python package to easily convert units of **Length** and **Mass**.  
It is designed for students, developers, and data scientists who need simple unit conversions in their projects.

---

## 📦 Features

- 🔁 **Length conversions**:  
  - Miles ↔ Kilometers  
  - Feet ↔ Inches  

- ⚖️ **Mass conversions**:  
  - Kilograms ↔ Tonnes  
  - Kilograms ↔ Pounds  

- 🧠 Simple function calls — no complex setup required  
- 📚 Built-in `help()` function to explore all available methods

---

## 🏗️ Module Structure

```

Conversion/
├── Length/
│   └── Lengthconversion.py
└── Mass/
    └── Massconversion.py

```

---

## 💻 Installation

You can install it **locally** from the source:

```bash
git clone https://github.com/subhrajeet06/Conversion.git
cd Conversion
pip install .
```

---

## 🧪 Usage

```python
from Conversion.Length import Lengthconversion as lc
from Conversion.Mass import Massconversion as mc

# Length Conversions
print(lc.miletokm(5))        # Output: 8.04672
print(lc.feettoinches(6))    # Output: 72.0

# Mass Conversions
print(mc.kgtotonne(1000))    # Output: 1.0
print(mc.kgtopound(5))       # Output: 11.0231

# Help
lc.help()
mc.help()
```

---

## 📌 Constants Used

* `1 mile = 1.609344 km`
* `1 foot = 12 inches`
* `1 kg = 0.001 tonne`
* `1 kg = 2.20462 pounds`

---

## 📚 Functions Available

### 📏 Length Module

* `miletokm(miles)`
* `kmtomile(kilometers)`
* `feettoinches(feet)`
* `inchestofeet(inches)`
* `help()`

### ⚖️ Mass Module

* `kgtotonne(kg)`
* `tonnetokg(tonne)`
* `kgtopound(kg)`
* `poundtokg(pound)`
* `help()`

---

## ✍️ Author

Made with ❤️ by **Subhrajeet** | 🎓 CS IT Student

---

## 🌟 Show Some Love

If you found this useful, **star ⭐ the repo** and share with your friends.
Have ideas or feedback? Feel free to open an issue or pull request!

---

## 📫 Connect with Me

* [Instagram](https://instagram.com/subhrajeet._.06)
* [LinkedIn](https://linkedin.com/in/subhrajeet-parida)
