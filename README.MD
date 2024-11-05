# Nail Salon Marketplace Data Scraper
I have a client called client is [Acrylics Worldwide](https://www.acrylicskawaii.world).
This project is a Python-based web scraper designed to gather business data from Google Maps for nail salons in specified cities. The application uses the Google Places API to pull business data and stores it in a SQLite database. The data is updated daily, and an API endpoint allows for generating an Excel file upon request. This project is built using Python, Flask, Docker, and is deployed on AWS.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Database Schema](#database-schema)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)

---

## Project Overview

This application collects and stores data about nail salons from Google Maps in five cities specified by the user. A daily cron job updates the database with new entries, and an API endpoint allows for generating an Excel spreadsheet of the stored data, which can be downloaded through a simple web interface.

## Features
- **Automated Data Collection**: Fetches business data daily from Google Maps using the Places API.
- **Database Storage**: Only stores unique entries, avoiding duplicate data.
- **API for Data Export**: Generates an Excel spreadsheet with the latest business data upon request.
- **Simple UI**: Provides a web interface for the client to download the Excel file.
- **Containerized Deployment**: Dockerized application, ready for deployment on AWS.

## Tech Stack
- **Backend**: Python, Flask
- **Database**: SQLite
- **API**: Google Places API
- **Containerization**: Docker, Docker Compose
- **Deployment**: AWS EC2
- **Automation**: Cron jobs for daily updates

## Architecture

1. **Flask API**: Handles data retrieval and export functionalities.
2. **SQLite Database**: Stores nail salon business information.
3. **Cron Job**: Runs daily to fetch and update data from Google Places API.
4. **Excel Generation**: Generates an Excel file from the database when requested.
5. **Docker and Docker Compose**: Manages application, database, and cron jobs in containers.
6. **AWS EC2**: Hosts the application.

## Setup and Installation

### Prerequisites
- Python 3.x
- Docker & Docker Compose
- Google Cloud account (for API key)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/nail-salon-marketplace-scraper.git
   cd nail-salon-marketplace-scraper