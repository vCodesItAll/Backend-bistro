![Database Table Representation](Screenshot%202023-11-10%20061902.png)

# Restaurant Menu API

## Basic Requirements

### Models
- Create models for MenuItems, Category, and Cuisine with the following fields:
  - Menu Items:
    - Title
    - Description
    - Price
    - Spicy Level
    - FK to Category
    - FK to Cuisine
  - Category:
    - Name (e.g., Appetizer, Dessert, Main Dish, etc.)
  - Cuisine:
    - Name (e.g., American, Thai, etc.)

### Views
- Implement views for READ operations on MenuItems.

### Routes
- Define routes that use the views created earlier.
- Example route:
  - `/api/menu-items/` - View full list of menu item information.

### JSON Response
- Ensure JSON response includes nested labels for category and cuisine.

### React Restaurant Code
- Change the URL in the React Restaurant Code to point to the Gitpod URL of your running backend code.
- Note: Do not write any React code for basic requirements.

# MoSCoW Prioritization

## Must Have
- Create models for MenuItems, Category, and Cuisine.
- Implement views for READ operations on MenuItems.
- Define routes for basic READ operations on MenuItems.
- JSON response with nested labels for category and cuisine.
- Change URL in React Restaurant Code to Gitpod backend URL.

## Shouldn't Have
- CRUD operations for MenuItems (Create, Update, Delete).
- Additional routes beyond basic requirements.

## Could Have
- Validation for input data.
- Error handling for API requests.
- Security measures for the API.

## Won't Have
- Advanced features beyond basic CRUD operations.
- User authentication and authorization.



