# Domain Model

Tracking bank transactions and expense statistics by category.

## Entities

- **Transaction** — a single operation (payment or income).
- **Category** — an expense/income category.

## Schema

```mermaid
erDiagram
    Category |o--o{ Transaction : "classifies"

    Category {
        int id PK
        string name
        string kind
        string color
    }
    Transaction {
        int id PK
        int category_id FK
        datetime occurred_at
        decimal amount
        string description
    }
```
