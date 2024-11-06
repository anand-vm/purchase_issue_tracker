# Product Damage History Module

## Overview

The **Product Damage History** module is an Odoo 17 custom module designed to manage information about damaged products received from suppliers. It provides a streamlined interface for recording, tracking, and managing damaged product information based on vendor bills, with options to add solutions and reasons for each case.

## Features

- Load damaged product items based on the selected vendor bill.
- Fields for vendor details, purchase order number, bill date, and solution.
- Itemized list with fields for quantity, reason, and remarks for each damaged item.
- Status bar with **Draft**, **Confirmed**, and **Closed** stages.
- Automatically loads items from the selected vendor bill and allows quantity adjustments.

## Installation

1. Place the module in your Odoo 17 addons directory.
2. Restart the Odoo server.
3. Go to the **Apps** menu in Odoo, search for "Product Damage History," and install the module.

## Usage

1. Navigate to **Damage History > Product Damage History** in the main menu.
2. Click **Create** to add a new record.
3. Select a **Vendor Bill** to load items automatically.
4. Add/edit quantities, reasons, and remarks as needed for each line item.
5. Save the record to finalize.

## Files

- `__init__.py`: Initializes the module.
- `__manifest__.py`: Defines metadata, dependencies, and other configurations for the module.
- `models/damage_history.py`: Contains the model definitions.
- `views/damage_history_view.xml`: Defines the form and tree views for the module.
- `views/menu.xml`: Creates menu items for accessing the module.

## Dependencies

- `base`
- `stock`
- `purchase`

## License

This module is provided as-is, under an open-source license. Modify and distribute freely as per your needs.

---

