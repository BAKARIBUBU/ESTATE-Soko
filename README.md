# Odoo Real Estate Module

## 📌 Overview

The **Odoo Real Estate** module is a property management system built for Odoo Ecosystem. It allows users to manage properties, property types, tags, and offers efficiently.

## 🚀 Features

- **Property Management**: Create, update, and manage properties.
- **Property Types**: Categorize properties based on their type.
- **Tags**: Assign custom tags to properties.
- **Offers**: Handle property offers and negotiations.
- **Sales Integration**: Convert offers into confirmed sales.
- **Access Control**: Different user roles and permissions.

## 📂 Module Structure

```
odoo_real_estate/
│── models/
│   ├── property.py
│   ├── property_type.py
│   ├── property_tag.py
│   ├── property_offer.py
│── views/
│   ├── property_views.xml
│   ├── property_type_views.xml
│   ├── property_tag_views.xml
│   ├── property_offer_views.xml
│── security/
│   ├── ir.model.access.csv
│── data/
│   ├── property_data.xml
│── __init__.py
│── __manifest__.py
```

## ⚙️ Installation

1. Copy the module folder to your Odoo `addons/` directory.
2. Restart the Odoo server:

   ```sh
   odoo-bin -c odoo.conf -u odoo_real_estate
   ```

3. Activate the **Developer Mode** in Odoo.
4. Navigate to **Apps** and install the module.

## 🛠 Usage

1. Go to **Real Estate** → **Properties** to manage properties.
2. Create or edit **Property Types** and **Tags** for categorization.
3. Navigate to **Offers** to track buyer negotiations.
4. Confirm offers to process sales.

## 🛡 Access Control

- **Administrator**: Full access to all features.
- **Property Manager**: Can manage properties and offers.
- **Sales Agent**: Can create and view offers.

## 📝 Configuration

- Modify `ir.model.access.csv` to customize permissions.
- Add demo data in `data/property_data.xml` for testing.

## 🎯 Future Enhancements

- Automated property valuation.
- Integration with accounting for invoicing.
- Customizable property reports.

## 🏆 Credits

Developed by **BAKARI**.

## 📄 License

This module is licensed under the **MIT License**.
