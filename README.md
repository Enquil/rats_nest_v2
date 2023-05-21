# Rats nest

## Table of Content

* [Project Description](https://github.com/Enquil/rats_nest_v2#project-description)
* [Planning](https://github.com/Enquil/rats_nest_v2#planning)
  * [Purpose](https://github.com/Enquil/rats_nest_v2#purpose)
  * [Core Functionality](https://github.com/Enquil/rats_nest_v2#purpose)
  * [Initial Timeframes](https://github.com/Enquil/rats_nest_v2#purpose)
* [Models](https://github.com/Enquil/rats_nest_v2#models)
  * [Product Domain](https://github.com/Enquil/rats_nest_v2#product-domain)
  * [Category](https://github.com/Enquil/rats_nest_v2#product-domain)
  * [SubCategory](https://github.com/Enquil/rats_nest_v2#product-domain)
  * [Product](https://github.com/Enquil/rats_nest_v2#product-domain)

***
***

## Project Description

***
***

## Planning

### ***Purpose***

### ***Core Functionality***

### ***Initial Timeframes***

***
***

## Models

* Identified Main Categories
  * Clothing
  * Equipment and Accessories
  * Supplements

### ***Category***

***Model Table***
|      Key      |             ValueType           |
| ------------- | ------------------------------- |
|     ID/PK     |             IntField            |
|     Parent    |         ForeignKey(Self)        |
|   Is_Parent   |              Boolean            |
|     Name      |         Text/CharField          |
| Friendly Name |         Text/CharField          |

### ***Product***

***Model Table***
|      Key      |             ValueType           |
| ------------- | ------------------------------- |
|     ID/PK     |             IntField            |
|      SKU      |             IntField            |
|    Category   |      ForeignKey (Category)      |
|     Name      |         Text/CharField          |
|     Brand     |            CharField            |
|  Description  |            TextField            |
| Feature List  |          Char/TextField         |
|  Male/Female  |            CharField            |
|   Has Size    |             Boolean             |
|   Image Url   |             IMG URL             |
|     Price     |           DecimalField          |
|     Rating    |           DecimalField          |

* If Man/Woman is None, product should be considered Unisex
* If has_size is true, need to differentiate between shoes and other clothing

***
***

## Design

***
***

## Bugs

***
***

## Future Implementation
