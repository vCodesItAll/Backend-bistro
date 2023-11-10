INSERT INTO categories (id, name) VALUES
(1, 'Appetizers'),
(2, 'Main Courses'),
(3, 'Desserts'),
(4, 'Beverages');

-- Insert statements for cuisines
INSERT INTO cuisines (id, name) VALUES
(1, 'Italian'),
(2, 'Mexican'),
(3, 'Chinese'),
(4, 'Indian');

-- Insert statements for menu_items
INSERT INTO menu_items (id, title, description, price, spicy_level, category_id, cuisine_id) VALUES
(1, 'Bruschetta', 'Toasted bread with tomatoes and basil', 8.99, 1, 1, 1),
(2, 'Chicken Quesadilla', 'Grilled chicken with cheese in a tortilla', 12.99, 2, 1, 2),
(3, 'Sweet and Sour Chicken', 'Battered chicken in sweet and sour sauce', 14.99, 3, 2, 3),
(4, 'Margherita Pizza', 'Tomato, mozzarella, and basil', 10.99, 1, 1, 1),
(5, 'Butter Chicken', 'Creamy tomato-based curry with chicken', 16.99, 2, 2, 4),
-- Add more menu items as needed
(100, 'Vegetarian Spring Rolls', 'Crispy spring rolls with vegetables', 9.99, 1, 1, 3),
(101, 'Beef and Broccoli', 'Stir-fried beef with broccoli in soy sauce', 15.99, 2, 2, 3),
-- Add more menu items as needed
(200, 'Tiramisu', 'Italian coffee-flavored dessert', 7.99, 1, 3, 1),
-- Add more menu items as needed
(300, 'Iced Tea', 'Refreshing cold tea', 2.99, NULL, 4, NULL);