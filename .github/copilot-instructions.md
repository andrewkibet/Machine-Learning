# GitHub Copilot Instructions for Machine Learning Workspace

## Workspace Overview

This workspace contains two distinct projects with different AI assistance policies:

### 1. **Lorna/** — Educational Capstone Assignments
- **Purpose:** Academic coursework for learning data science fundamentals
- **Policy:** ⚠️ **NO AI-GENERATED CODE** — Students must write all code themselves
- **Context:** Instructor: Abishek Ganesh; Due: December 18, 2025
- **AI Use Allowed:**
  - ✅ Guidance on Python concepts and documentation
  - ✅ Debugging hints and error explanations
  - ✅ Clarification of assignment requirements
  - ✅ Data structure and algorithm recommendations (not implementations)
  - ❌ Code generation, solutions, or complete implementations
- **Written Reflections:** Students must answer conceptual questions in their own words

### 2. **23/** — Fruit Classification Flask Application
- **Purpose:** Production/portfolio ML project
- **Policy:** ✅ Full AI assistance available
- **Architecture:** Flask backend + Web UI + ML model serving
- **Key Files:**
  - `main.py`: Flask API for fruit prediction (loads `fruits.pickle`)
  - `index.html`: Web interface with prediction form
  - `citrus.csv`: Training dataset
  - `script.js`, `style.css`: Frontend files

### 3. **README.md** — Project Documentation
- Focus: Machine Learning applications in cybersecurity
- Resources: Kaggle datasets and models

---

## File Structure

```
Machine-Learning/
├── README.md                          # Project overview
├── .git/                              # Git repository
├── .gitattributes                     # Git line endings config
├── 23/                                # Flask ML project (AI OK)
│   ├── main.py                        # Flask backend
│   ├── main.ipynb                     # Jupyter notebook
│   ├── index.html                     # Web UI
│   ├── style.css                      # Styling
│   ├── script.js                      # Frontend logic
│   ├── citrus.csv                     # Dataset
│   └── fruits.pickle                  # Trained ML model
└── Lorna/                             # Educational assignments (NO AI CODE)
    ├── incremental-capstone-unit-1.ipynb
    └── incremental-capstone-unit-2.ipynb
```

---

## Guidelines for AI Assistance

### For **/Lorna/** (Educational—Learning Focus)

**When working on capstone assignments:**

1. **Code Implementation:** You MUST write your own code. AI should NOT generate complete solutions.
2. **Debugging:** AI can explain syntax errors or suggest where to look, but not write fixes.
3. **Concepts:** Ask about data structures, algorithms, or Python features before implementing.
4. **Testing:** AI can help you write test cases and edge case ideas.
5. **Reflection Responses:** You must answer written reflection questions in your own words.

**Example Allowed Interactions:**
- ❌ "Complete the `clean_product_data()` function for me"
- ✅ "I'm getting a TypeError when converting prices. What does this error mean?"
- ✅ "Should I use a Set or List to find unique customers? Why?"
- ✅ "Show me how `statistics.mode()` works in Python"

### For **/23/** (Production—Full Assistance)

**When working on the Flask application:**

1. All AI code generation, refactoring, and debugging is welcome
2. Performance optimization and best practices are encouraged
3. Documentation and testing suggestions are helpful

---

## Development Environment

### Required Packages

**For /23/ (Flask Project):**
```
flask
flask-cors
numpy
pickle (stdlib)
```

**For /Lorna/ (Assignments):**
```
statistics (stdlib)
```

### Running the Flask Application (23/)

```bash
cd 23/
python main.py
```

Server runs on `http://localhost:5000`

---

## Key Conventions

### Python Style

- **Format:** Follow PEP 8 standards
- **Comments:** Explain *why*, not just *what*
- **Functions:** Include docstrings with Args and Returns
- **Testing:** Use `assert` statements for verification
- **Notebooks:** Separate markup (markdown cells) from code

### Assignment Structure (Lorna/)

- Each part has:
  - **Problem Description** (context)
  - **Example Verification** (inputs/expected outputs)
  - **Implementation Section** (student code)
  - **Basic Tests** (pre-built `assert` statements)
  - **Written Reflection** (conceptual questions)

Students should add their own edge case tests beyond the basic verification.

### Project Structure (23/)

- Flask routes defined in `main.py`
- Frontend logic in `script.js`
- Styling in `style.css`
- Models persisted as `.pickle` files
- Data stored in `.csv` format

---

## Common Tasks & Hints

### Assignment Help (Lorna/)

- **Data Cleaning:** Use `.strip()`, `.lower()`, string slicing
- **Statistics:** Import `statistics` module; review `mean()`, `median()`, `mode()`, `stdev()`
- **Collections:** Review when to use List, Set, Dict
- **Classes:** Understand `__init__()` and instance methods
- **Nested Loops:** Practice with lists of lists for weekly sales

### Flask Improvements (23/)

- Current TODO: Move model loading outside the prediction function for performance
- Error handling: Add try/catch for missing JSON fields
- CORS config: Fix typo in `resorces` → `resources`
- API documentation: Swagger/OpenAPI would be helpful

---

## AI Interaction Preferences

- **Lorna assignments:** Thought-partner mode (guide without code)
- **23 project:** Full engineering mode (code generation OK)
- **Questions:** Always clarify which folder/context applies
- **Ambiguity:** If unclear whether code is for a capstone, ask first

---

## Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Python Statistics Module](https://docs.python.org/3/library/statistics.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- Kaggle: Dataset and competition platform
