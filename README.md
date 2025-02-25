# Real Estate MVP: Next.js 14 & Django with Docker

## Overview

This project is a Real Estate Management MVP built using Django REST Framework and Next.js 14 (React), fully containerized with Docker and served via NGINX. It integrates TypeScript, Redux, RTK Query, and other modern technologies to create a scalable and efficient property management solution.

## Key Features

- **Backend:** Django & Django REST Framework for API development
- **Frontend:** Next.js 14 (React) with TypeScript
- **State Management:** Redux & Redux Toolkit (RTK Query)
- **Containerization:** Docker for both backend and frontend
- **Reverse Proxy:** NGINX to serve API and Next.js client
- **Authentication & Authorization:** Secure login for landlords, tenants, and maintenance staff
- **Issue Reporting System:** Tenants can report maintenance issues
- **Technician Assignment & Tracking:** Landlords can track service requests
- **Tenant Marketplace:** A controlled environment for tenant-to-tenant transactions
- **Incident Reporting:** Report tenancy agreement violations

## Background

The inspiration for this project comes from real-life inefficiencies in managing apartment complexes.

In many rental properties, communication between landlords, tenants, and maintenance teams is chaotic. This MVP is designed to:

- Streamline issue reporting
- Improve maintenance tracking
- Enhance communication
- Provide a structured marketplace for tenants

By leveraging modern web technologies, this project aims to solve key challenges in real estate management.

## Tech Stack

### Backend
- Django
- Django REST Framework
- PostgreSQL (or SQLite for development)
- Celery & Redis (for background tasks)

### Frontend
- Next.js 14 (React)
- TypeScript
- Redux & RTK Query
- Tailwind CSS

### Infrastructure
- Docker & Docker Compose
- NGINX (Reverse Proxy)
- Shell Scripting for automation

## Setup & Installation

### Prerequisites
Ensure you have the following installed:

- Python 3.9+
- Node.js 18+
- Docker & Docker Compose

### Installation Steps

1. Clone the repository:
   ```sh
   git clone git@github.com:IlyasOsman/RentalHub.git
   cd RentlHub

### Set up environment variables:

   ```sh
      cp .env.example .env
   ```
### Update the .env file with your configuration.

### Build and start the Docker containers:

  ```sh
      make build
   ```

### Run database migrations:

   ```sh
      make migrate
   ```

### Create a superuser for Django Admin:

   ```sh
   make superuser
   ```
### Access the application:

#### Frontend: http://localhost:3000
#### Backend API: http://localhost:8000/api/
#### Admin Panel: http://localhost:8000/admin/