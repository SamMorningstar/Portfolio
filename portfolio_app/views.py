from django.shortcuts import get_object_or_404, render
from .models import PortfolioItem


def home(request):
    items = PortfolioItem.objects.all()
    return render(request, "home.html", {"portfolio_items": items})


def project_detail(request, slug):
    project = get_object_or_404(PortfolioItem, slug=slug)
    return render(request, "project_detail.html", {"project": project})


def about(request):
    return render(
        request,
        "about.html",
        {
            "name": "Mohammed Nabil Chaudhary",
            "bio": "Full Stack Web Developer with 5+ years of experience building scalable, production-ready web applications using React, Node.js, and AWS. Specialized in RESTful API development, database optimization, authentication systems, and cloud deployment. Proven track record of delivering 20+ client projects with strong performance, clean architecture, and high reliability",
            "skills": ["Django", "Python", "SQL", "HTML", "CSS", "Node.js", "Full Stack Development", "MERN Stack", "JavaScript (ES6+)", "React.js", "Node.js", "Express.js", "RESTful APIs", "JWT", "Authentication", "MongoDB", "MySQL", "AWS Cloud Deployment", "CI/CD", "Git", "Agile/Scrum", "API Integration", "Performance Optimization", "Scalable System Design"],
        },
    )
