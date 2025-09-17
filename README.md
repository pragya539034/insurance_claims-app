>#  Insurance Claims Processing System

> A simple Flask + Docker web application to submit insurance claims with a clean Bootstrap-powered interface.

> # Objective

> To build a user-friendly web application for submitting insurance claims.

>Provide a form-based UI where users can enter policy details, claim type, amount, description, and upload documents.

>Ensure easy deployment using Docker for consistent environments.

># Tools Used

>Flask (Python) → Backend web framework.

>Jinja2 Templates → Used with Flask to render dynamic HTML pages.

>Bootstrap 5 → CSS & JS framework for responsive and modern UI design.

>Docker → Containerization for consistent deployment.

>HTML5 & CSS → Structure and styling of web pages.

># Steps Included
> structure
<img width="230" height="168" alt="image" src="https://github.com/user-attachments/assets/5f50ac81-c203-45a5-bd63-c2dc59f514de" />

>1.Setup Project

>- Create app.py as the main Flask entry point.

>- Define routes for submitting and rendering claims.

>2.Design Templates

>- Create index.html inside templates/.

>- Use Bootstrap 5 for responsive layout and form design.

>- Integrate Jinja2 for rendering dynamic content.

>3.Containerization with Docker

>- Make a Dockerfile to containerize the app.

>- Expose Flask app on port .

>- Run inside Docker for portability

> 4.Run Application in CMD

>` cd directory path`

>`docker build -t image_name .`

>`docker -d -p portno.:portno. image_name`

># Key Insights

>- Bootstrap 5 provides ready-made UI components, reducing the need for manual CSS.

>- Jinja2 templates make it easy to inject dynamic data from Flask into HTML pages.

>- Docker ensures the app runs consistently across different machines.

># Conclusion

>- Build a simple yet effective Flask web application.

>- Use Bootstrap 5 for a professional, responsive UI.

>- Leverage Jinja2 templates for dynamic content rendering.

>- Package and deploy applications using Docker for reliability and scalability
