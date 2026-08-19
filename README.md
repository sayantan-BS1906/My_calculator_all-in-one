# 🧮 All-in-One Advanced Calculator

A comprehensive, multi-mode calculator application available in both **HTML/JavaScript (Web)** and **Python (Desktop)** versions.

## 📋 Features Overview

### 🌐 **Web Version** (`my-calculator-all-in-one.html`)
- Beautiful responsive design with gradient UI
- Runs in any modern web browser
- No installation required
- Real-time calculations
- Mobile-friendly interface

### 🖥️ **Python Version** (`my-calculator_python_version.py`)
- Desktop GUI application using Tkinter
- Advanced numerical computing with SciPy
- Professional scientific interface
- Cross-platform (Windows, macOS, Linux)

---

## 🎯 Calculator Modes

### 📐 **Scientific Mode**
✅ **Trigonometric Functions**
- `sin(x)`, `cos(x)`, `tan(x)`, `asin(x)`, `acos(x)`, `atan(x)`

✅ **Hyperbolic Functions**
- `sinh(x)`, `cosh(x)`, `tanh(x)`

✅ **Logarithmic Operations**
- Natural logarithm: `ln(x)`
- Common logarithm: `log(x)` (base 10)

✅ **Power Operations**
- Exponentiation: `x^y` or `x**y`
- Square root: `√x` or `sqrt(x)`
- Cube root: `∛x` or `cbrt(x)`
- Squared: `x²`
- Cubed: `x³`

✅ **Angle Modes**
- Degrees (DEG) - default
- Radians (RAD)
- Gradians (GRAD)

✅ **Mathematical Constants**
- π (Pi) = 3.14159265359
- e (Euler's number) = 2.71828182846

✅ **Advanced Functions**
- Factorial: `n!`
- Absolute value: `|x|`
- Reciprocal: `1/x`
- Exponential: `e^x`

---

### 💰 **Commercial Mode**

1. **Discount Calculator**
   - Calculate discount amount and final price
   - Formula: `Final Price = Price - (Price × Discount% / 100)`

2. **Profit/Loss Analyzer**
   - Analyze profit or loss
   - Calculate percentage gain/loss
   - Formula: `Profit/Loss = Selling Price - Cost Price`

3. **Interest Calculator**
   - **Simple Interest**: `SI = (P × R × T) / 100`
   - **Compound Interest**: `A = P(1 + R/100N)^(NT)`
   - Where: P = Principal, R = Rate, T = Time, N = Frequency

4. **Mark-up Calculator**
   - Calculate selling price with mark-up
   - Formula: `Selling Price = Cost + (Cost × Mark-up% / 100)`

5. **Percentage Change**
   - Calculate percentage change between values
   - Formula: `% Change = ((New Value - Old Value) / Old Value) × 100`

---

### ∫ **Calculus Mode**

1. **Numerical Integration** (Trapezoidal Rule)
   - Calculate: `∫[a,b] f(x)dx`
   - Approximates area under curve
   - Adjustable intervals for accuracy

2. **Numerical Derivative** (Central Difference)
   - Calculate: `∂f/∂x at point x`
   - Formula: `f'(x) ≈ [f(x+h) - f(x-h)] / 2h`

3. **Series Summation** (∑)
   - Sum expressions from start to end
   - Example: `∑[1,10] i²` = 1² + 2² + ... + 10² = 385

4. **Simpson's Rule** (Advanced Integration)
   - More accurate numerical integration
   - Uses parabolic approximations

---

### ⚡ **Basic Mode**
- Standard arithmetic: `+`, `−`, `×`, `÷`, `%`
- Parentheses support: `(` `)`
- Memory operations: `MC`, `M+`, `M−`, `MR`
- Simple and fast calculations

---

## 🚀 Quick Start

### **Web Version**

1. **Online (Vercel Deployment)**
   - Visit: https://my-calculator-all-in-one.netlify.app
   - No installation needed!

2. **Local Browser**
   ```bash
   # Download and open in browser
   open advanced-calculator.html
   # or
   double-click advanced-calculator.html
   ```

### **Python Version**

1. **Install Dependencies**
   ```bash
   pip install scipy numpy
   # Tkinter usually comes with Python
   ```

2. **Run Calculator**
   ```bash
   python calculator.py
   ```

3. **Or make it executable** (Linux/macOS)
   ```bash
   chmod +x calculator.py
   ./calculator.py
   ```

---

## 📦 Installation

### Requirements for Python Version

**Python 3.7+** with the following libraries:

```
scipy>=1.5.0
numpy>=1.19.0
```

**Installation:**
```bash
# Option 1: Install all at once
pip install -r requirements.txt

# Option 2: Install individually
pip install scipy numpy
```

### Browser Compatibility (Web Version)

| Browser | Status |
|---------|--------|
| Chrome | ✅ Fully Supported |
| Firefox | ✅ Fully Supported |
| Safari | ✅ Fully Supported |
| Edge | ✅ Fully Supported |
| Opera | ✅ Fully Supported |
| IE 11 | ⚠️ Limited Support |

---

## 📖 Usage Examples

### Scientific Mode Examples

```
sin(45)           → 0.7071 (in degrees)
2^10              → 1024
sqrt(16)          → 4
ln(2.718)         → 1
factorial(5)      → 120
π                 → 3.14159
e^2               → 7.389
```

### Commercial Mode Examples

```
Discount: Price=100, Discount=10%      → Final Price: ₹90
Profit/Loss: Cost=100, Selling=150     → Profit: ₹50, 50%
Simple Interest: P=1000, R=5%, T=2     → SI: ₹100
Compound Interest: P=1000, R=5%, T=2   → CI: ₹102.5
Mark-up: Cost=100, Mark-up=20%         → Selling: ₹120
% Change: Old=100, New=150             → 50% increase
```

### Calculus Mode Examples

```
∫[0,1] x² dx              → 0.333333 (using Trapezoidal Rule)
∂/∂x [x³] at x=2         → 12
∑[1,10] i²               → 385
Simpson's Rule [0,2] x²  → 2.666667
```

---

## 🧠 Memory Functions

| Function | Description | Example |
|----------|-------------|---------|
| **MC** | Memory Clear | Sets memory to 0 |
| **M+** | Memory Add | Current value + Memory |
| **M−** | Memory Subtract | Memory - Current value |
| **MR** | Memory Recall | Display memory value |

---

## 🎨 Button Color Legend

| Color | Purpose |
|-------|---------|
| Gray | Number buttons (0-9) |
| Purple | Operators (+, −, ×, ÷) |
| Blue | Scientific functions |
| Red | Commercial functions |
| Teal/Green | Calculus functions |
| Green | Equals (=) button |
| Red | Clear (C) button |
| Orange | Delete (DEL) button |
| Yellow | Parentheses ( ) |

---

## 📁 File Structure

```
My_calculator_all-in-one/
│
├── index.html                  # Landing page
├── advanced-calculator.html    # Web calculator (main)
├── calculator.py               # Python desktop calculator
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE                     # License information
```

---

## 🔧 Technical Details

### Web Version Stack
- **HTML5** - Structure
- **CSS3** - Styling with gradients
- **JavaScript (Vanilla)** - Logic & calculations
- **No frameworks** - Lightweight & fast

### Python Version Stack
- **Tkinter** - GUI framework
- **SciPy** - Scientific computing (integration, derivatives)
- **NumPy** - Numerical operations
- **Math** - Standard mathematical functions

---

## ⚙️ Advanced Features

### Expression Support
- **Web Version**: Full mathematical expression evaluation
- **Python Version**: Direct Python expression evaluation with safety checks

### Numerical Methods
- **Trapezoidal Rule**: For integration
- **Simpson's Rule**: For more accurate integration
- **Central Difference**: For numerical derivatives
- **Series Summation**: For discrete summations

### Error Handling
- Division by zero protection
- Invalid expression detection
- Input validation
- User-friendly error messages

---

## 🐛 Known Limitations

1. **Large Factorial Numbers**: Factorial(n) becomes slow for n > 20000
2. **Integration Accuracy**: Depends on number of intervals (higher = more accurate)
3. **Derivative Accuracy**: Best results near smooth points in functions
4. **Python Version**: Requires manual closing of application

---

## 🚀 Future Enhancements

- [ ] Matrix operations
- [ ] Statistical functions (mean, median, std dev)
- [ ] Graph/plot capabilities
- [ ] Unit conversion
- [ ] Loan calculator
- [ ] Currency converter
- [ ] Dark mode theme
- [ ] Multiple languages

---

## 📚 Educational Use

This calculator is perfect for:
- ✅ Mathematics students
- ✅ Physics and Engineering students
- ✅ Finance and Commerce professionals
- ✅ Scientific computing learners
- ✅ Programming education

---

## 📄 License

This project is **free to use and modify** for personal or commercial projects.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Make improvements
3. Submit pull requests
4. Report bugs
5. Suggest new features

---

## 💬 Feedback & Support

If you encounter any issues or have suggestions:
1. Open an issue on GitHub
2. Check existing issues for solutions
3. Provide detailed error messages and steps to reproduce

---

## 👨‍💻 Developer

Created with ❤️ by **Sayantan Chakraborty**

**Repository**: https://github.com/sayantan-BS1906/My_calculator_all-in-one  
**Live Demo**: https://my-calculator-all-in-one.vercel.app

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Modes | 4 |
| Scientific Functions | 20+ |
| Commercial Calculators | 5 |
| Calculus Operations | 4 |
| Lines of Code (HTML) | 600+ |
| Lines of Code (Python) | 700+ |
| Browser Support | 99% |

---

## ✨ Highlights

🎯 **Multi-Platform**: Web + Desktop versions  
⚡ **Fast & Responsive**: No lag, instant calculations  
📱 **Mobile Friendly**: Works on all devices  
🔒 **Safe**: No data collection or external requests  
🎨 **Beautiful UI**: Modern gradient design  
📖 **Well Documented**: Comprehensive README  
🆓 **Free & Open Source**: No hidden costs  

---

**Enjoy calculating! 🎉**

*Last Updated: August 17, 2026*
