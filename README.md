# selenium-project

### 📌 **Project Description**

This project is a **Python-based Selenium WebDriver script** that automates testing for the [Demoblaze](https://www.demoblaze.com) e-commerce website. The script performs a series of automated actions to validate the website's core functionalities and captures visual evidence through screenshots.

---

### 🚀 **Features & Actions**

#### 1️⃣ **Login Test**
- Logs into the website using predefined credentials.
- Verifies successful authentication.

#### 2️⃣ **Category Selection**
- Selects the **"Laptops"** category.
- Ensures the category filter displays the correct items.

#### 3️⃣ **Navigation Testing**
- **About Us:** Navigates to the **About Us** section and verifies the displayed content.  
- **Contact Page:** Opens the **Contact** page and confirms the content is correctly loaded.  

#### 4️⃣ **Contact Form Submission**
- Fills the form with sample data.  
- Submits the form and handles the confirmation alert.  
- Verifies the form submission is successful.  

#### 5️⃣ **Screenshots**
- Captures screenshots after key actions to document the website's state:
    - `laptopfilter.png` → After filtering laptops.  
    - `about.png` → On the **About Us** section.  
    - `Contact.png` → On the **Contact** form page.  

---

### 🛠️ **Technologies Used**
- **Language:** Python  
- **Automation Framework:** Selenium WebDriver  
- **Browser:** Firefox  
- **Output:** Screenshots for visual validation  

---

### ✅ **Usage Instructions**
1. **Install Dependencies:**  
```bash
pip install -r requirements.txt
```

2. **Run the Script:**  
```bash
python3 test.py
```

3. **Review Screenshots:**  
- Check the `screenshots` folder for the captured images.  

---

### 📝 **Conclusion**
This script effectively automates the testing of **Demoblaze** website features, including **login, category filtering, page navigation, and form submission**, while capturing screenshots for visual validation.
