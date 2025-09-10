# Algorithm Rules for Processing Belgrade Instagram Links

## Overview
This document describes the algorithm used to process Instagram links of Belgrade bars, cafes, and cool places to create a structured markdown table.

## Algorithm Steps

### 1. Data Collection
- **Input**: Instagram profile URL
- **Process**: 
  - Access Instagram profile page
  - Extract business name from profile handle or bio
  - Read bio/description for place type indicators
  - Look for menu items, food photos, or service descriptions
  - Check for location information in bio or posts

### 2. Place Type Classification
Analyze the following indicators to determine place type:

#### Cafe
- Keywords: "cafe", "kafana", "coffee", "kafa", "espresso", "latte"
- Visual indicators: Coffee cups, pastries, breakfast items
- Serbian terms: "kafana", "kafić"

#### Restaurant
- Keywords: "restaurant", "restoran", "kitchen", "kuhinja"
- Visual indicators: Full meals, dining tables, formal setting
- Menu items: Main courses, appetizers, desserts

#### Bar
- Keywords: "bar", "pub", "pivnica", "cocktail", "drinks"
- Visual indicators: Alcohol bottles, bar counter, drinks
- Serbian terms: "bar", "pivnica", "kafana" (traditional Serbian bar)

#### Fast Food
- Keywords: "fast food", "brza hrana", "burger", "pizza", "gyros"
- Visual indicators: Quick service, takeaway containers
- Menu focus: Single-item specialties

#### Other
- Keywords: "bistro", "market", "food court", "specialty"
- Visual indicators: Mixed or unique concept
- Unclear classification from available information

### 3. Description Generation
- **Length**: 1-2 sentences maximum
- **Content**: 
  - Primary cuisine type or specialty
  - Notable features (atmosphere, unique items)
  - Target audience or vibe
- **Language**: English, with Serbian terms when culturally relevant

### 4. Google Maps Link Generation
- **Method 1**: Search by business name + "Belgrade" on Google Maps
- **Method 2**: If address found in Instagram bio, search by address
- **Method 3**: Search by Instagram handle + "Belgrade" as fallback
- **Format**: Use Google Maps share link format

### 5. Quality Assurance
- Verify place name accuracy
- Ensure type classification matches visual evidence
- Confirm Google Maps link leads to correct location
- Check description is concise and informative

## Error Handling
- If Instagram profile is private/inaccessible: Mark as "Profile not accessible"
- If Google Maps search fails: Leave Google Maps field empty with note
- If type unclear: Use "other" category
- If description insufficient: Use generic description based on type

## Output Format
```markdown
| Place Name | Type | Description | Instagram Link | Google Maps Link |
|------------|------|-------------|----------------|------------------|
```

## File Organization
- **belgradeMap.md**: Contains only the raw Instagram links list
- **places.md**: Contains only the analysis table (no headers, descriptions, or additional content)
- **.ai/rules.md**: Contains the algorithm documentation

### File Structure Rules
1. **belgradeMap.md**: 
   - Contains ALL Instagram links (both processed and unprocessed)
   - Maintains the original complete list
   - Clean list format

2. **places.md**:
   - Only the markdown table with analyzed places
   - No headers, titles, or additional content
   - Pure table format for easy processing

3. **.ai/rules.md**:
   - Algorithm documentation
   - Processing rules
   - File organization guidelines

## Future Modifications
This algorithm can be modified by:
1. Adding new place type categories
2. Updating keyword lists for classification
3. Changing description length or style
4. Adding new data sources for verification
5. Implementing automated Google Maps API integration