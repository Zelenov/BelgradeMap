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
- **Method 1**: Search for the exact place on Google Maps and get the direct place link
- **Method 2**: If address found in Instagram bio, search by address and get place link
- **Method 3**: Search by Instagram handle + "Belgrade" as fallback and get place link
- **Format**: Use direct Google Maps place links (not search links)
- **Link Format**: `https://www.google.com/maps/place/[PlaceName]/@[coordinates]/data=![place_data]?entry=ttu`
- **Avoid**: Search links like `https://maps.google.com/?q=...`
- **Prefer**: Direct place links that show exact location with coordinates and place ID

#### Google Maps Link Generation Process:

**Method 1: Using Google Place ID (Recommended)**
1. **Find Place ID**: Use Google's Place ID Finder tool (https://developers.google.com/maps/documentation/places/web-service/place-id)
2. **Search by Business Name**: Enter business name + "Belgrade" in the Place ID Finder
3. **Get Place ID**: Copy the unique Place ID (e.g., `ChIJ3S-JXmauEmsRUcIaWtf4MzE`)
4. **Generate Direct Link**: Use format `https://www.google.com/maps/place/[PlaceName]/@[coordinates]/data=![place_data]?entry=ttu`
5. **Alternative Format**: Use `https://maps.google.com/?cid=[CID]` if available

**Method 2: Manual Google Maps Search**
1. **Search on Google Maps**: Go to maps.google.com and search for business name
2. **Click on Place Marker**: Click the exact business marker (not search results)
3. **Get Share Link**: Click "Share" button and copy the direct place link
4. **Verify Format**: Ensure it's a direct place link, not a search link

**Method 2.1: Multi-Stage Instagram Profile Parsing (Universal Algorithm)**
This method applies to ALL Instagram profiles and follows a systematic approach:

**Stage 1: Profile Analysis**
1. **Visit Instagram Profile**: Go to the business Instagram profile
2. **Check Bio Section**: Look for Google Maps link in the bio/description
3. **Check Story Highlights**: Look for "Location" or "Address" highlights
4. **Check Recent Posts**: Look for location tags or address mentions
5. **Check Contact Info**: Look for address in contact information

**Stage 2: Link Extraction**
1. **Parse Direct Link**: Extract the Google Maps link from the profile
2. **Verify Link Format**: Ensure it's a direct place link with coordinates
3. **Check Link Quality**: Verify the link contains place data and coordinates

**Stage 3: Link Validation**
1. **Test Link**: Click the link to ensure it works
2. **Verify Location**: Confirm it shows the correct business location
3. **Check Coordinates**: Ensure coordinates are present in the URL

**Stage 4: Table Update**
1. **Replace Search Link**: Replace any existing search link with direct place link
2. **Update Address Text**: Use the actual address from the Google Maps link
3. **Verify Format**: Ensure the link follows the correct format

**Method 3: Using Google Places API (For Developers)**
1. **Text Search API**: Use Places API Text Search to find place
2. **Get Place Details**: Use Place Details API with `googleMapsLinks.placeUri` field
3. **Extract Direct Link**: Use the pre-formatted URL from API response

#### Link Quality Indicators:
- ✅ Contains coordinates (@44.xxx,20.xxx)
- ✅ Contains place data (!4m6!3m5!1s0x...)
- ✅ Has entry=ttu parameter
- ✅ Uses /place/ format (not /search/)
- ❌ Avoids search format (?q=...)
- ❌ Avoids generic location links
- ❌ Avoids /dir/ format (directions links)

#### Link Format Examples:
- **Good**: `https://www.google.com/maps/place/PizzaBar/@44.7983383,20.4675602,17z/data=!4m6!3m5!1s0x475a700b56686e65:0x9a2859bfeede7e96!8m2!3d44.7983383!4d20.4701351!16s%2Fg%2F11c73c3yw6?entry=ttu`
- **Good**: `https://maps.google.com/?cid=3545450935484072529`
- **Bad**: `https://maps.google.com/?q=Pizza+Bar+Belgrade`

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
| Place Name | Type | Description | Instagram Link | Address |
|------------|------|-------------|----------------|---------|
| [Place Name] | [Type] | [Description] | [@username](https://www.instagram.com/username/) | [Address](https://www.google.com/maps/place/PlaceName/@coordinates/data=!place_data?entry=ttu) |
```

## File Organization
- **belgradeMap.md**: Contains only the raw Instagram links list
- **README.md**: Contains the analysis table with proper formatting
- **.ai/rules.md**: Contains the algorithm documentation

### File Structure Rules
1. **belgradeMap.md**: 
   - Contains ALL Instagram links (both processed and unprocessed)
   - Maintains the original complete list
   - Clean list format

2. **README.md**:
   - Contains the markdown table with analyzed places
   - Instagram links formatted as [@username](full_instagram_url)
   - Address links formatted as [address_text](direct_google_maps_place_url)
   - No "Belgrade" in address text (since it's implied)

3. **.ai/rules.md**:
   - Algorithm documentation
   - Processing rules
   - File organization guidelines

## Implementation Status

### Current Implementation:
- ✅ **Pizza Bar Serbia**: Updated with direct Google Maps place link
- ✅ **Peers Belgrade**: Updated with direct Google Maps place link
- ✅ **Shine S Cleaning**: Updated with direct Google Maps place link
- ✅ **Ruske Palačinke**: Updated with direct Google Maps place link (Blinok, Novi Sad)
- ✅ **Voulez-Vous**: Updated with direct Google Maps place link

### Algorithm Successfully Applied:
1. ✅ **Applied Multi-Stage Algorithm**: Used Method 2.1 (Multi-Stage Instagram Profile Parsing) for ALL businesses
2. ✅ **Processed Each Profile**: Followed the 4-stage process for every Instagram profile in the table
3. ✅ **Extracted Direct Links**: Got Google Maps links directly from Instagram profiles and business websites
4. ✅ **Updated All Entries**: Replaced search links with direct place links for all businesses
5. ✅ **Verified All Links**: All links now use proper Google Maps place format with coordinates

### Universal Application:
- **All Businesses**: Apply the multi-stage algorithm to every Instagram profile
- **Systematic Approach**: Follow the same 4-stage process for consistency
- **Quality Assurance**: Ensure all links meet the quality indicators
- **No Exceptions**: Every business gets the same thorough treatment
- **Alternative**: Search for Belgrade location with same Instagram handle

## Future Modifications
This algorithm can be modified by:
1. Adding new place type categories
2. Updating keyword lists for classification
3. Changing description length or style
4. Adding new data sources for verification
5. Implementing automated Google Maps API integration
6. **Automating Place ID lookup** using Google Places API
7. **Batch processing** for multiple businesses at once