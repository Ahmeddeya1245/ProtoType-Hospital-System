# Hospital Management System

A Python-based command-line application for managing hospital patients and specializations. This system helps hospitals organize patient queues across different specializations while considering patient urgency levels.

## Features

- Patient Management
  - Add new patients with different urgency levels (normal, urgent, super urgent)
  - Remove patients from the queue
  - Smart queue organization based on patient urgency
  - Maximum queue size of 10 patients per specialization

- Specialization Support
  - Support for multiple medical specializations
  - Each specialization maintains its own patient queue
  - Prioritized patient handling based on urgency level

- Patient Status Tracking
  - Three levels of urgency:
    - Normal (0)
    - Urgent (1)
    - Super Urgent (2)
  - Automatic queue reorganization based on patient status

## Usage

1. Run the program:
```bash
python hospital_management.py
```

2. Available Options:
   - Add new patient (Option 1)
   - Print all patients (Option 2)
   - Get next patient (Option 3)
   - Remove a leaving patient (Option 4)
   - End the program (Option 5)

### Adding a Patient
1. Select Option 1
2. Enter specialization number
3. Enter patient name
4. Enter status (0 for normal, 1 for urgent, 2 for super urgent)

### Viewing Patients
- Select Option 2 to see all patients organized by specialization
- Each specialization shows the count of patients and their details

### Processing Next Patient
1. Select Option 3
2. Enter specialization number
3. System will return the next patient in queue based on urgency

### Removing a Patient
1. Select Option 4
2. Enter specialization number
3. Enter patient name
4. Confirm removal

## Classes

### Patient
- Represents individual patients with name and status
- Includes string representation and comparison methods

### Hospital
- Manages specializations and patient queues
- Handles patient addition, removal, and queue organization
- Implements smart sorting based on urgency

### FrontendManager
- Provides command-line interface
- Handles user input and program flow
- Includes demo data for testing

## Requirements
- Python 3.x
- No additional packages required

## Implementation Details

- The system implements a priority queue mechanism where patients are automatically sorted based on urgency
- Each specialization can handle up to 10 patients
- Patient urgency levels affect their position in the queue
- The system includes input validation for all user inputs
- Built-in demo data for testing functionality

## Contributing
[Ahmed Diaa]
