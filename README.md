# Educational Portal - Flask Login App

A beautiful and responsive Flask web application featuring a 3-column login interface for students, teachers, and colleges.

## Features

- **Modern UI Design**: Beautiful gradient background with glass-morphism effects
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Three User Types**: Separate login forms for Students, Teachers, and Colleges
- **Registration System**: Complete registration forms for all user types
- **Interactive Elements**: Hover effects, animations, and smooth transitions
- **Flash Messages**: Success and error notifications
- **Font Awesome Icons**: Professional icons for better user experience
- **Form Validation**: Client-side password confirmation and required field validation

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── login.html        # Main login page with 3 columns
│   ├── register.html     # Registration page with 3 columns
│   └── dashboard.html    # Dashboard page after login
└── static/
    └── style.css         # CSS styles for the application
```

## Usage

### Login
1. **Choose your role**: Select from Student, Teacher, or College login
2. **Enter credentials**: Fill in your username and password
3. **Submit**: Click the login button to access your dashboard
4. **Dashboard**: You'll be redirected to a personalized dashboard

### Registration
1. **Click Register**: Use the "Register" links on the login page
2. **Choose your role**: Select the appropriate registration form
3. **Fill in details**: Complete all required fields with your information
4. **Submit**: Click the register button to create your account
5. **Login**: After successful registration, you can login with your credentials

## Customization

- **Colors**: Modify the CSS variables in `static/style.css` to change the color scheme
- **Icons**: Replace Font Awesome icons with your preferred icon set
- **Validation**: Add proper authentication logic in the `login()` function in `app.py`
- **Registration**: Implement backend registration logic in the `register()` function in `app.py`
- **Database**: Integrate with a database for user management
- **Email Verification**: Add email confirmation for new registrations

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6.0
- **Fonts**: Google Fonts (Poppins)

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This project is open source and available under the MIT License. 