CREATE TABLE "categories" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "cuisines" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "menu_items" (
  "id" integer PRIMARY KEY,
  "title" varchar,
  "description" varchar,
  "price" float,
  "spicy_level" integer,
  "category_id" integer,
  "cuisine_id" integer
);

ALTER TABLE "menu_items" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");

ALTER TABLE "menu_items" ADD FOREIGN KEY ("cuisine_id") REFERENCES "cuisines" ("id");
