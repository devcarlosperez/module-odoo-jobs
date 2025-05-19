# Task and Job Management System

## Description

This project consists of two interconnected Odoo modules that provide functionality for managing tasks and job positions in an organization. The modules handle employee management, task assignments, job positions, and categories.

## Modules

### Task Manager Module
Features:
- Employee profiles with personal information
- Task creation and assignment
- Task priority levels (Low, Medium, High)
- Deadline tracking for tasks
- Many-to-many relationship between employees and tasks
- Integration with job positions

### Jobs Module
Features:
- Job position management
- Job category organization
- Department integration with HR module
- Employment types (Full-time, Part-time, Freelance, Intern)
- Salary tracking
- One-to-many relationship between categories and positions

## Getting Started

1. Clone this project in a new folder: ```git clone https://github.com/devcarlosperez/module-odoo-jobs-task-manager```
2. Navigate to the project folder: ```cd module-odoo-jobs-task-manager```
3. Start the container ```docker compose up -d```

## Build With

- *Odoo 18*
- *Docker*
- *Docker Compose*

## Acknowledgments

Special thanks to Professor Tiburcio for his guidance and feedback, and to my classmates for their support and ideas throughout development.

## Author

Carlos Luis Pérez Santana