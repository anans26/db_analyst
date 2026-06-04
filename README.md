# Database AI Agent

An AI-powered database assistant that enables users to query databases using natural language. The project combines PostgreSQL, Python, SQLAlchemy, and LLM-based agents to translate user questions into SQL queries and return meaningful results.

## Features

* Natural language database querying
* PostgreSQL database integration
* Schema-aware query generation
* Query validation and safety checks
* Result formatting and presentation
* Sample database generation for testing

## Tech Stack

* Python 3.11
* PostgreSQL
* Docker
* SQLAlchemy
* OpenAI API
* Git & GitHub

## Current Project Structure

```text
AI-DB/
│
├── schema/
│   ├── layer1.sql
│   ├── layer2.sql
│   ├── layer3.sql
│   └── layer4.sql
│
├── scripts/
│   ├── create_schema_v2.py
│   ├── inspect_tables.py
│   └── seed_v2.py
│
├── agent.py
├── validator.py
├── formatter.py
├── main.py
├── db.py
│
├── schema_design.md
├── docker-compose.yml
└── README.md
```

## Database Schema

The current implementation uses a logistics and supply chain dataset consisting of:

* regions
* employees
* suppliers
* customers
* carriers
* products
* warehouses
* inventory
* orders
* order_items
* shipments

The schema serves as a realistic environment for testing database agent capabilities.

## Setup

### Start PostgreSQL

```bash
docker compose up -d
```

### Create Database Schema

```bash
python scripts/create_schema_v2.py
```

### Verify Tables

```bash
python scripts/inspect_tables.py
```

### Seed Sample Data

```bash
python scripts/seed_v2.py
```

## Current Progress

### Completed

* Database schema design
* Multi-layer schema implementation
* Foreign key relationships
* Constraints and validations
* Seed script development
* Initial data generation

### In Progress

* Large-scale data generation
* Database agent implementation
* Query validation system
* Result formatting
* Natural language to SQL workflow

## Future Goals

* Convert natural language into SQL queries
* Query explanation and validation
* Multi-database support
* Analytics and reporting capabilities
* Conversational database interaction


