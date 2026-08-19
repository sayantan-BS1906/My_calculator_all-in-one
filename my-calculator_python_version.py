import math
import tkinter as tk
from tkinter import messagebox, ttk


class AdvancedCalculatorApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Advanced Scientific & Commercial Calculator")
        self.geometry("520x720")
        self.configure(bg="#667eea")

        # Calculator State
        self.current_input = "0"
        self.memory = 0.0
        self.angle_mode = "deg"

        self._build_ui()

    def _build_ui(self):
        # Header
        header = tk.Label(
            self,
            text="Advanced Scientific & Commercial Calculator",
            bg="#764ba2",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            pady=10,
        )
        header.pack(fill=tk.X, padx=10, pady=(10, 5))

        # Main Display
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            self,
            textvariable=self.display_var,
            bg="#2d3436",
            fg="#00ff88",
            font=("Courier New", 20, "bold"),
            anchor="e",
            padx=15,
            pady=15,
        )
        self.display.pack(fill=tk.X, padx=10, pady=5)

        # Memory Bar
        mem_frame = tk.Frame(self, bg="#ecf0f1", pady=4, padx=8)
        mem_frame.pack(fill=tk.X, padx=10, pady=2)

        self.mem_var = tk.StringVar(value="Memory: 0.00")
        tk.Label(
            mem_frame,
            textvariable=self.mem_var,
            bg="#ecf0f1",
            fg="#667eea",
            font=("Segoe UI", 9, "bold"),
        ).pack(side=tk.LEFT)

        btn_box = tk.Frame(mem_frame, bg="#ecf0f1")
        btn_box.pack(side=tk.RIGHT)
        for label, cmd in [
            ("MC", self.mem_clear),
            ("M+", self.mem_add),
            ("M-", self.mem_sub),
            ("MR", self.mem_recall),
        ]:
            tk.Button(
                btn_box,
                text=label,
                command=cmd,
                font=("Segoe UI", 8),
                padx=4,
                pady=1,
            ).pack(side=tk.LEFT, padx=2)

        # Tabbed Mode Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Mode Frames
        self.tab_scientific = tk.Frame(self.notebook, bg="white")
        self.tab_commercial = tk.Frame(self.notebook, bg="white")
        self.tab_calculus = tk.Frame(self.notebook, bg="white")
        self.tab_vectors = tk.Frame(self.notebook, bg="white")

        self.notebook.add(self.tab_scientific, text="Scientific")
        self.notebook.add(self.tab_commercial, text="Commercial")
        self.notebook.add(self.tab_calculus, text="Calculus")
        self.notebook.add(self.tab_vectors, text="Vectors")

        self._build_scientific_tab()
        self._build_commercial_tab()
        self._build_calculus_tab()
        self._build_vectors_tab()

    # ==================== DISPLAY & PARSING HELPERS ====================
    def update_display(self):
        text = (
            self.current_input[:27] + "..."
            if len(self.current_input) > 30
            else self.current_input
        )
        self.display_var.set(text)

    def append_char(self, char):
        if self.current_input == "0" and char not in [".", "+", "-", "*", "/"]:
            self.current_input = char
        else:
            self.current_input += char
        self.update_display()

    def clear_display(self):
        self.current_input = "0"
        self.update_display()

    def delete_last(self):
        self.current_input = (
            self.current_input[:-1] if len(self.current_input) > 1 else "0"
        )
        self.update_display()

    def toggle_sign(self):
        if self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display()

    def eval_math_expression(self, expr, x_val=None):
        """Safe numerical expression evaluation."""
        safe_env = {
            "sin": lambda v: (
                math.sin(math.radians(v))
                if self.angle_mode == "deg"
                else math.sin(v)
            ),
            "cos": lambda v: (
                math.cos(math.radians(v))
                if self.angle_mode == "deg"
                else math.cos(v)
            ),
            "tan": lambda v: (
                math.tan(math.radians(v))
                if self.angle_mode == "deg"
                else math.tan(v)
            ),
            "asin": lambda v: (
                math.degrees(math.asin(v))
                if self.angle_mode == "deg"
                else math.asin(v)
            ),
            "acos": lambda v: (
                math.degrees(math.acos(v))
                if self.angle_mode == "deg"
                else math.acos(v)
            ),
            "atan": lambda v: (
                math.degrees(math.atan(v))
                if self.angle_mode == "deg"
                else math.atan(v)
            ),
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "cbrt": lambda v: math.copysign(abs(v) ** (1 / 3), v),
            "factorial": math.factorial,
            "abs": abs,
            "exp": math.exp,
            "pow": pow,
            "pi": math.pi,
            "e": math.e,
        }
        if x_val is not None:
            safe_env["x"] = x_val

        clean = (
            expr.replace("^", "**")
            .replace("π", "pi")
            .replace("÷", "/")
            .replace("×", "*")
        )
        return eval(clean, {"__builtins__": {}}, safe_env)

    def calculate(self):
        try:
            res = self.eval_math_expression(self.current_input)
            self.current_input = str(round(res, 8))
        except Exception:
            self.current_input = "Error"
        self.update_display()

    # ==================== MEMORY ====================
    def mem_clear(self):
        self.memory = 0.0
        self.mem_var.set("Memory: 0.00")

    def mem_add(self):
        try:
            self.memory += float(self.eval_math_expression(self.current_input))
            self.mem_var.set(f"Memory: {self.memory:.2f}")
        except Exception:
            pass

    def mem_sub(self):
        try:
            self.memory -= float(self.eval_math_expression(self.current_input))
            self.mem_var.set(f"Memory: {self.memory:.2f}")
        except Exception:
            pass

    def mem_recall(self):
        self.current_input = str(self.memory)
        self.update_display()

    # ==================== SCIENTIFIC TAB ====================
    def _build_scientific_tab(self):
        frame = self.tab_scientific

        # Angle toggles
        top_bar = tk.Frame(frame, bg="white")
        top_bar.pack(fill=tk.X, pady=5)
        self.angle_lbl = tk.Label(
            top_bar,
            text="Angle: DEG",
            bg="white",
            fg="#667eea",
            font=("Segoe UI", 9, "bold"),
        )
        self.angle_lbl.pack(side=tk.LEFT, padx=10)

        tk.Button(
            top_bar,
            text="Toggle DEG/RAD",
            command=self.toggle_angle_mode,
            font=("Segoe UI", 8),
        ).pack(side=tk.RIGHT, padx=10)

        # Buttons grid
        grid_frame = tk.Frame(frame, bg="white")
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        buttons = [
            ("sin(", "sin"),
            ("cos(", "cos"),
            ("tan(", "tan"),
            ("ln(", "ln"),
            ("log(", "log"),
            ("asin(", "asin"),
            ("acos(", "acos"),
            ("atan(", "atan"),
            ("sqrt(", "√"),
            ("^", "x^y"),
            ("sinh(", "sinh"),
            ("cosh(", "cosh"),
            ("tanh(", "tanh"),
            ("factorial(", "n!"),
            ("exp(", "e^x"),
            ("π", "π"),
            ("e", "e"),
            ("abs(", "|x|"),
            ("+/-", "+/-"),
            ("C", "C"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("/", "÷"),
            ("DEL", "DEL"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("*", "×"),
            ("%", "%"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("-", "-"),
            ("(", "("),
            ("0", "0"),
            (".", "."),
            ("=", "="),
            ("+", "+"),
            (")", ")"),
        ]

        for i, (val, text) in enumerate(buttons):
            r, c = divmod(i, 5)
            cmd = lambda v=val: self._on_btn_click(v)
            bg_col = (
                "#00ff88"
                if text == "="
                else (
                    "#ff6b6b"
                    if text == "C"
                    else (
                        "#3498db"
                        if any(
                            fn in text
                            for fn in [
                                "sin",
                                "cos",
                                "tan",
                                "ln",
                                "log",
                                "√",
                                "n!",
                                "e^x",
                                "π",
                                "e",
                                "|x|",
                                "x^y",
                            ]
                        )
                        else "#ecf0f1"
                    )
                )
            )
            fg_col = (
                "white"
                if bg_col in ["#3498db", "#ff6b6b"]
                else ("#2d3436" if bg_col == "#00ff88" else "black")
            )

            btn = tk.Button(
                grid_frame,
                text=text,
                command=cmd,
                bg=bg_col,
                fg=fg_col,
                font=("Segoe UI", 9, "bold"),
                width=5,
                height=1,
            )
            btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")

        for i in range(5):
            grid_frame.columnconfigure(i, weight=1)
        for i in range(8):
            grid_frame.rowconfigure(i, weight=1)

    def toggle_angle_mode(self):
        self.angle_mode = "rad" if self.angle_mode == "deg" else "deg"
        self.angle_lbl.config(text=f"Angle: {self.angle_mode.upper()}")

    def _on_btn_click(self, val):
        if val == "=":
            self.calculate()
        elif val == "C":
            self.clear_display()
        elif val == "DEL":
            self.delete_last()
        elif val == "+/-":
            self.toggle_sign()
        else:
            self.append_char(val)

    # ==================== COMMERCIAL TAB ====================
    def _build_commercial_tab(self):
        frame = self.tab_commercial

        def create_entry_row(parent, label1, label2):
            f = tk.Frame(parent, bg="white")
            f.pack(fill=tk.X, pady=2)
            tk.Label(f, text=label1, bg="white", width=14, anchor="w").pack(
                side=tk.LEFT
            )
            e1 = tk.Entry(f, width=8)
            e1.pack(side=tk.LEFT, padx=4)
            tk.Label(f, text=label2, bg="white", width=14, anchor="w").pack(
                side=tk.LEFT
            )
            e2 = tk.Entry(f, width=8)
            e2.pack(side=tk.LEFT, padx=4)
            return e1, e2

        # 1. Discount
        lbl_d = tk.Label(
            frame,
            text="💰 Discount Calculator",
            font=("Segoe UI", 9, "bold"),
            bg="white",
            fg="#e74c3c",
        )
        lbl_d.pack(anchor="w", padx=10, pady=(6, 0))
        d_p, d_pct = create_entry_row(frame, "Original Price:", "Discount %:")
        d_res = tk.Label(
            frame, text="", bg="#fef5f1", fg="#e74c3c", font=("Segoe UI", 9)
        )
        d_res.pack(fill=tk.X, padx=10)

        def calc_discount():
            try:
                p, d = float(d_p.get()), float(d_pct.get())
                amt = p * (d / 100)
                d_res.config(
                    text=f"Discount: ₹{amt:.2f} | Final Price: ₹{(p - amt):.2f}"
                )
            except Exception:
                d_res.config(text="Invalid inputs")

        tk.Button(
            frame,
            text="Calculate Discount",
            command=calc_discount,
            bg="#e74c3c",
            fg="white",
        ).pack(fill=tk.X, padx=10, pady=2)

        # 2. Profit / Loss
        lbl_pl = tk.Label(
            frame,
            text="📊 Profit/Loss Calculator",
            font=("Segoe UI", 9, "bold"),
            bg="white",
            fg="#e74c3c",
        )
        lbl_pl.pack(anchor="w", padx=10, pady=(6, 0))
        pl_cp, pl_sp = create_entry_row(frame, "Cost Price:", "Selling Price:")
        pl_res = tk.Label(
            frame, text="", bg="#fef5f1", fg="#e74c3c", font=("Segoe UI", 9)
        )
        pl_res.pack(fill=tk.X, padx=10)

        def calc_pl():
            try:
                cp, sp = float(pl_cp.get()), float(pl_sp.get())
                diff = sp - cp
                pct = (diff / cp) * 100
                t = "Profit" if diff >= 0 else "Loss"
                pl_res.config(text=f"{t}: ₹{abs(diff):.2f} | {t} %: {pct:.2f}%")
            except Exception:
                pl_res.config(text="Invalid inputs")

        tk.Button(
            frame,
            text="Calculate P/L",
            command=calc_pl,
            bg="#e74c3c",
            fg="white",
        ).pack(fill=tk.X, padx=10, pady=2)

        # 3. Simple & Compound Interest
        lbl_int = tk.Label(
            frame,
            text="💳 Interest Calculator",
            font=("Segoe UI", 9, "bold"),
            bg="white",
            fg="#e74c3c",
        )
        lbl_int.pack(anchor="w", padx=10, pady=(6, 0))
        i_p, i_r = create_entry_row(frame, "Principal (P):", "Rate (R %):")
        i_t, i_n = create_entry_row(frame, "Time (Years):", "Freq (n/yr):")
        i_res = tk.Label(
            frame, text="", bg="#fef5f1", fg="#e74c3c", font=("Segoe UI", 9)
        )
        i_res.pack(fill=tk.X, padx=10)

        def calc_si():
            try:
                p, r, t = float(i_p.get()), float(i_r.get()), float(i_t.get())
                si = (p * r * t) / 100
                i_res.config(
                    text=f"Simple Interest: ₹{si:.2f} | Total: ₹{(p + si):.2f}"
                )
            except Exception:
                i_res.config(text="Invalid inputs")

        def calc_ci():
            try:
                p, r, t, n = (
                    float(i_p.get()),
                    float(i_r.get()),
                    float(i_t.get()),
                    float(i_n.get() or 1),
                )
                tot = p * ((1 + r / (100 * n)) ** (n * t))
                i_res.config(
                    text=f"Compound Interest: ₹{(tot - p):.2f} | Total: ₹{tot:.2f}"
                )
            except Exception:
                i_res.config(text="Invalid inputs")

        btn_row = tk.Frame(frame, bg="white")
        btn_row.pack(fill=tk.X, padx=10, pady=2)
        tk.Button(
            btn_row,
            text="Simple Interest",
            command=calc_si,
            bg="#e74c3c",
            fg="white",
            width=18,
        ).pack(side=tk.LEFT, expand=True)
        tk.Button(
            btn_row,
            text="Compound Interest",
            command=calc_ci,
            bg="#e74c3c",
            fg="white",
            width=18,
        ).pack(side=tk.RIGHT, expand=True)

    # ==================== CALCULUS TAB ====================
    def _build_calculus_tab(self):
        frame = self.tab_calculus

        tk.Label(
            frame,
            text="ƒ(x) Function Workspace",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#16a085",
        ).pack(anchor="w", padx=10, pady=(6, 2))

        f_row = tk.Frame(frame, bg="white")
        f_row.pack(fill=tk.X, padx=10, pady=2)
        tk.Label(
            f_row,
            text="f(x) =",
            bg="white",
            font=("Segoe UI", 9, "bold"),
            fg="#117a65",
        ).pack(side=tk.LEFT)
        self.fn_input = tk.Entry(f_row, font=("Courier New", 10))
        self.fn_input.insert(0, "x^2 + 2*x + 1")
        self.fn_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=6)

        # Operations
        bounds_frame = tk.Frame(frame, bg="white")
        bounds_frame.pack(fill=tk.X, padx=10, pady=4)

        tk.Label(bounds_frame, text="a (Lower):", bg="white").grid(
            row=0, column=0
        )
        self.c_a = tk.Entry(bounds_frame, width=6)
        self.c_a.insert(0, "0")
        self.c_a.grid(row=0, column=1, padx=4)

        tk.Label(bounds_frame, text="b (Upper):", bg="white").grid(
            row=0, column=2
        )
        self.c_b = tk.Entry(bounds_frame, width=6)
        self.c_b.insert(0, "1")
        self.c_b.grid(row=0, column=3, padx=4)

        tk.Label(bounds_frame, text="Point x:", bg="white").grid(
            row=0, column=4
        )
        self.c_x = tk.Entry(bounds_frame, width=6)
        self.c_x.insert(0, "2")
        self.c_x.grid(row=0, column=5, padx=4)

        self.calc_res = tk.Label(
            frame,
            text="Result will appear here",
            bg="#d5f4e6",
            fg="#16a085",
            font=("Segoe UI", 9, "bold"),
            pady=6,
        )
        self.calc_res.pack(fill=tk.X, padx=10, pady=6)

        # Calculus Action Buttons
        grid_c = tk.Frame(frame, bg="white")
        grid_c.pack(fill=tk.X, padx=10)

        calc_actions = [
            ("∫ Integral (Simpson)", self.calc_integral),
            ("d/dx Derivative", self.calc_derivative),
            ("f″(x) 2nd Deriv", self.calc_second_derivative),
            ("Tangent Line", self.calc_tangent),
            ("Root (Bisection)", self.calc_root),
            ("Arc Length", self.calc_arc_length),
        ]

        for i, (label, cmd) in enumerate(calc_actions):
            r, c = divmod(i, 2)
            tk.Button(
                grid_c,
                text=label,
                command=cmd,
                bg="#16a085",
                fg="white",
                font=("Segoe UI", 8, "bold"),
            ).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
        grid_c.columnconfigure(0, weight=1)
        grid_c.columnconfigure(1, weight=1)

    def calc_integral(self):
        try:
            expr = self.fn_input.get()
            a, b = float(self.c_a.get()), float(self.c_b.get())
            n = 1000
            h = (b - a) / n
            total = self.eval_math_expression(
                expr, a
            ) + self.eval_math_expression(expr, b)
            for i in range(1, n):
                val = self.eval_math_expression(expr, a + i * h)
                total += (2 if i % 2 == 0 else 4) * val
            ans = h * total / 3
            self.calc_res.config(text=f"∫[{a}, {b}] f(x) dx ≈ {ans:.8f}")
        except Exception as e:
            self.calc_res.config(text="Evaluation Error")

    def calc_derivative(self):
        try:
            expr = self.fn_input.get()
            x = float(self.c_x.get())
            h = 1e-5
            f1 = self.eval_math_expression(expr, x + h)
            f2 = self.eval_math_expression(expr, x - h)
            d = (f1 - f2) / (2 * h)
            self.calc_res.config(text=f"f′({x}) ≈ {d:.8f}")
        except Exception:
            self.calc_res.config(text="Evaluation Error")

    def calc_second_derivative(self):
        try:
            expr = self.fn_input.get()
            x = float(self.c_x.get())
            h = 1e-4
            f0 = self.eval_math_expression(expr, x)
            f1 = self.eval_math_expression(expr, x + h)
            f2 = self.eval_math_expression(expr, x - h)
            d2 = (f1 - 2 * f0 + f2) / (h * h)
            self.calc_res.config(text=f"f″({x}) ≈ {d2:.8f}")
        except Exception:
            self.calc_res.config(text="Evaluation Error")

    def calc_tangent(self):
        try:
            expr = self.fn_input.get()
            x0 = float(self.c_x.get())
            y0 = self.eval_math_expression(expr, x0)
            h = 1e-5
            m = (
                self.eval_math_expression(expr, x0 + h)
                - self.eval_math_expression(expr, x0 - h)
            ) / (2 * h)
            b = y0 - m * x0
            sign = "+" if b >= 0 else "-"
            self.calc_res.config(
                text=f"Tangent at x={x0}: y = {m:.4f}x {sign} {abs(b):.4f}"
            )
        except Exception:
            self.calc_res.config(text="Evaluation Error")

    def calc_root(self):
        try:
            expr = self.fn_input.get()
            a, b = float(self.c_a.get()), float(self.c_b.get())
            fa, fb = self.eval_math_expression(
                expr, a
            ), self.eval_math_expression(expr, b)
            if fa * fb > 0:
                self.calc_res.config(text="Root must bracket a sign change!")
                return
            for _ in range(100):
                mid = (a + b) / 2
                fmid = self.eval_math_expression(expr, mid)
                if abs(fmid) < 1e-9 or abs(b - a) < 1e-9:
                    break
                if fa * fmid <= 0:
                    b = mid
                    fb = fmid
                else:
                    a = mid
                    fa = fmid
            self.calc_res.config(text=f"Root in [{a:.2f}, {b:.2f}] ≈ {mid:.8f}")
        except Exception:
            self.calc_res.config(text="Evaluation Error")

    def calc_arc_length(self):
        try:
            expr = self.fn_input.get()
            a, b = float(self.c_a.get()), float(self.c_b.get())
            n = 500
            h = (b - a) / n
            total = 0
            for i in range(n + 1):
                x = a + i * h
                d = (
                    self.eval_math_expression(expr, x + 1e-5)
                    - self.eval_math_expression(expr, x - 1e-5)
                ) / 2e-5
                term = math.sqrt(1 + d * d)
                total += (
                    (1 if (i == 0 or i == n) else (2 if i % 2 == 0 else 4))
                    * term
                )
            ans = h * total / 3
            self.calc_res.config(text=f"Arc Length on [{a}, {b}] ≈ {ans:.6f}")
        except Exception:
            self.calc_res.config(text="Evaluation Error")

    # ==================== VECTORS TAB ====================
    def _build_vectors_tab(self):
        frame = self.tab_vectors

        tk.Label(
            frame,
            text="🧮 Vector Operations (comma separated: x, y, z)",
            bg="white",
            font=("Segoe UI", 9, "bold"),
            fg="#8e44ad",
        ).pack(anchor="w", padx=10, pady=(6, 2))

        f_in = tk.Frame(frame, bg="white")
        f_in.pack(fill=tk.X, padx=10, pady=2)
        tk.Label(f_in, text="Vector A:", bg="white").grid(row=0, column=0)
        self.vec_a = tk.Entry(f_in, width=12)
        self.vec_a.insert(0, "1,2,3")
        self.vec_a.grid(row=0, column=1, padx=4)

        tk.Label(f_in, text="Vector B:", bg="white").grid(row=0, column=2)
        self.vec_b = tk.Entry(f_in, width=12)
        self.vec_b.insert(0, "4,5,6")
        self.vec_b.grid(row=0, column=3, padx=4)

        tk.Label(f_in, text="Scalar k:", bg="white").grid(row=1, column=0)
        self.vec_k = tk.Entry(f_in, width=12)
        self.vec_k.insert(0, "2")
        self.vec_k.grid(row=1, column=1, padx=4, pady=4)

        self.vec_res = tk.Label(
            frame,
            text="",
            bg="#f5eef8",
            fg="#8e44ad",
            font=("Segoe UI", 9, "bold"),
            pady=6,
        )
        self.vec_res.pack(fill=tk.X, padx=10, pady=6)

        grid_v = tk.Frame(frame, bg="white")
        grid_v.pack(fill=tk.X, padx=10)

        vec_actions = [
            ("A + B", self.v_add),
            ("A - B", self.v_sub),
            ("A · B (Dot)", self.v_dot),
            ("A × B (Cross)", self.v_cross),
            ("k · A", self.v_scalar),
            ("|A| & |B| Mag", self.v_mag),
            ("∠(A, B) Angle", self.v_angle),
            ("Proj A on B", self.v_proj),
        ]

        for i, (label, cmd) in enumerate(vec_actions):
            r, c = divmod(i, 2)
            tk.Button(
                grid_v,
                text=label,
                command=cmd,
                bg="#8e44ad",
                fg="white",
                font=("Segoe UI", 8, "bold"),
            ).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
        grid_v.columnconfigure(0, weight=1)
        grid_v.columnconfigure(1, weight=1)

    def _parse_vec(self, entry):
        return [float(x.strip()) for x in entry.get().split(",") if x.strip()]

    def v_add(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            self.vec_res.config(
                text=f"A + B = ({', '.join(str(x + y) for x, y in zip(a, b))})"
            )
        except Exception:
            self.vec_res.config(text="Dimension mismatch or invalid input")

    def v_sub(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            self.vec_res.config(
                text=f"A - B = ({', '.join(str(x - y) for x, y in zip(a, b))})"
            )
        except Exception:
            self.vec_res.config(text="Dimension mismatch or invalid input")

    def v_dot(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            dot = sum(x * y for x, y in zip(a, b))
            self.vec_res.config(text=f"A · B = {dot:.4f}")
        except Exception:
            self.vec_res.config(text="Dimension mismatch or invalid input")

    def v_cross(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            if len(a) == 3 and len(b) == 3:
                c = [
                    a[1] * b[2] - a[2] * b[1],
                    a[2] * b[0] - a[0] * b[2],
                    a[0] * b[1] - a[1] * b[0],
                ]
                self.vec_res.config(text=f"A × B = ({c[0]}, {c[1]}, {c[2]})")
            else:
                self.vec_res.config(text="Cross product requires 3D vectors")
        except Exception:
            self.vec_res.config(text="Error calculating cross product")

    def v_scalar(self):
        try:
            a = self._parse_vec(self.vec_a)
            k = float(self.vec_k.get())
            self.vec_res.config(
                text=f"k · A = ({', '.join(str(k * x) for x in a)})"
            )
        except Exception:
            self.vec_res.config(text="Invalid vector or scalar")

    def v_mag(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            mag_a = math.sqrt(sum(x * x for x in a))
            mag_b = math.sqrt(sum(x * x for x in b))
            self.vec_res.config(text=f"|A| = {mag_a:.4f} | |B| = {mag_b:.4f}")
        except Exception:
            self.vec_res.config(text="Invalid vector input")

    def v_angle(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            dot = sum(x * y for x, y in zip(a, b))
            mag_a = math.sqrt(sum(x * x for x in a))
            mag_b = math.sqrt(sum(x * x for x in b))
            cos_t = max(-1.0, min(1.0, dot / (mag_a * mag_b)))
            rad = math.acos(cos_t)
            deg = math.degrees(rad)
            self.vec_res.config(text=f"∠(A, B) = {deg:.2f}° ({rad:.4f} rad)")
        except Exception:
            self.vec_res.config(text="Angle calculation error")

    def v_proj(self):
        try:
            a, b = self._parse_vec(self.vec_a), self._parse_vec(self.vec_b)
            dot = sum(x * y for x, y in zip(a, b))
            mag_sq = sum(x * x for x in b)
            scale = dot / mag_sq
            proj = [round(x * scale, 4) for x in b]
            self.vec_res.config(text=f"proj_B(A) = ({', '.join(map(str, proj))})")
        except Exception:
            self.vec_res.config(text="Projection calculation error")


if __name__ == "__main__":
    app = AdvancedCalculatorApp()
    app.mainloop()