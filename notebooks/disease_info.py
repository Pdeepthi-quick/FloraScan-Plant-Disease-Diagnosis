# Disease info dictionary (trimmed for brevity, you can keep the full version as in your original code)
disease_info = {
    "Apple___Apple_scab": {
        "symptoms": "Olive-green to black velvety spots on leaves and fruit; premature leaf drop.",
        "remedy": "Plant resistant varieties, apply fungicides early, remove fallen leaves to reduce spores."
    },
    "Apple___Black_rot": {
        "symptoms": "Purple leaf spots, rotting fruit, and branch cankers.",
        "remedy": "Prune infected branches, remove mummified fruits, and maintain tree health."
    },
    "Apple___Cedar_apple_rust": {
        "symptoms": "Bright orange leaf spots and fruit deformities.",
        "remedy": "Remove nearby junipers, apply fungicides like Myclobutanil in spring."
    },
    "Apple___healthy": {
        "symptoms": "No visible signs of infection or damage.",
        "remedy": "Maintain tree health with pruning, proper watering, and pest monitoring."
    },
    "Blueberry___healthy": {
        "symptoms": "No leaf spots or mold, vibrant green foliage.",
        "remedy": "Use acidic soil (pH 4.5–5.5), full sun, mulch to retain moisture."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "symptoms": "White powdery growth on leaves and shoots; leaf curling.",
        "remedy": "Prune for air flow, apply sulfur-based fungicides, avoid overhead watering."
    },
    "Cherry_(including_sour)___healthy": {
        "symptoms": "Shiny green leaves, normal fruit development.",
        "remedy": "Regular pruning and monitoring; ensure sunlight and air circulation."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "symptoms": "Gray elongated lesions on leaves; leaf yellowing.",
        "remedy": "Rotate crops, use resistant hybrids, apply fungicides if needed."
    },
    "Corn_(maize)___Common_rust_": {
        "symptoms": "Reddish-brown pustules on leaves.",
        "remedy": "Use resistant varieties, apply fungicides early if needed."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "symptoms": "Cigar-shaped gray-green leaf lesions; yield reduction.",
        "remedy": "Plant resistant varieties and apply fungicides during early growth."
    },
    "Corn_(maize)___healthy": {
        "symptoms": "Upright, green leaves with no lesions.",
        "remedy": "Proper spacing, fertilization, and early disease monitoring."
    },
    "Grape___Black_rot": {
        "symptoms": "Brown leaf lesions, black shriveled fruit (mummies).",
        "remedy": "Remove mummies, prune infected canes, use protective fungicides."
    },
    "Grape___Esca_(Black_Measles)": {
        "symptoms": "Interveinal leaf yellowing, black spots on berries, sudden vine collapse.",
        "remedy": "Remove infected vines, avoid wet pruning, apply fungicides."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "symptoms": "Circular brown spots on leaves leading to drop.",
        "remedy": "Prune affected leaves, apply neem or fungicides, ensure airflow."
    },
    "Grape___healthy": {
        "symptoms": "Healthy green leaves with no spotting.",
        "remedy": "Regular pruning and monitoring for mildew or pests."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "symptoms": "Yellowing leaves, bitter misshapen fruit, branch dieback.",
        "remedy": "Remove infected trees, control psyllids, follow quarantine protocols."
    },
    "Peach___Bacterial_spot": {
        "symptoms": "Water-soaked, angular leaf and fruit lesions.",
        "remedy": "Apply copper sprays, use resistant varieties, avoid overhead irrigation."
    },
    "Peach___healthy": {
        "symptoms": "Glossy green leaves and unblemished fruit.",
        "remedy": "Prune for airflow, water at base, inspect regularly for disease."
    },
    "Pepper,_bell___Bacterial_spot": {
        "symptoms": "Dark, water-soaked spots on leaves and fruits.",
        "remedy": "Use clean seeds, apply copper fungicides, avoid wet field work."
    },
    "Pepper,_bell___healthy": {
        "symptoms": "Dark green foliage and shiny peppers.",
        "remedy": "Proper spacing, avoid water on foliage, fertilize adequately."
    },
    "Potato___Early_blight": {
        "symptoms": "Dark spots with concentric rings on older leaves.",
        "remedy": "Apply fungicides, remove infected leaves, rotate crops."
    },
    "Potato___Late_blight": {
        "symptoms": "Water-soaked leaf lesions, white mold underneath; tuber rot.",
        "remedy": "Remove infected plants, apply fungicides, avoid water splashing."
    },
    "Potato___healthy": {
        "symptoms": "Even, green foliage with no spots or curling.",
        "remedy": "Hilling, good drainage, certified disease-free seeds."
    },
    "Raspberry___healthy": {
        "symptoms": "Vigorous growth and green foliage with no signs of stress.",
        "remedy": "Mulch to retain moisture, prune after harvest, monitor pests."
    },
    "Soybean___healthy": {
        "symptoms": "Upright green leaves and normal flowering.",
        "remedy": "Timely irrigation, crop rotation, monitor aphids and rust."
    },
    "Squash___Powdery_mildew": {
        "symptoms": "White powdery spots on leaves and stems.",
        "remedy": "Apply sulfur or neem sprays, improve airflow, avoid wetting foliage."
    },
    "Strawberry___Leaf_scorch": {
        "symptoms": "Dark purple spots with light centers on leaves.",
        "remedy": "Use drip irrigation, remove infected leaves, apply fungicides."
    },
    "Strawberry___healthy": {
        "symptoms": "Lush green foliage with firm, clean fruit.",
        "remedy": "Maintain soil moisture, mulch with straw, remove old leaves."
    },
    "Tomato___Bacterial_spot": {
        "symptoms": "Small, dark, water-soaked spots on leaves and fruits.",
        "remedy": "Avoid overhead watering, apply copper sprays, destroy infected plants."
    },
    "Tomato___Early_blight": {
        "symptoms": "Dark concentric rings on lower leaves, leaf yellowing.",
        "remedy": "Prune lower leaves, apply fungicides, rotate crops."
    },
    "Tomato___Late_blight": {
        "symptoms": "Water-soaked lesions, white mold under leaves, rapid leaf and fruit rot.",
        "remedy": "Destroy infected plants, apply systemic fungicides, control humidity."
    },
    "Tomato___Leaf_Mold": {
        "symptoms": "Yellowing upper leaf surfaces, fuzzy gray mold underneath.",
        "remedy": "Improve ventilation, apply fungicides, avoid overhead watering."
    },
    "Tomato___Septoria_leaf_spot": {
        "symptoms": "Small, circular leaf spots with dark borders and gray centers.",
        "remedy": "Remove lower infected leaves, apply chlorothalonil or copper fungicides."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "symptoms": "Stippling and webbing on leaves, leaf drop.",
        "remedy": "Spray with miticides or neem oil, increase humidity, introduce ladybugs."
    },
    "Tomato___Target_Spot": {
        "symptoms": "Brown circular spots with target-like rings on leaves and fruit.",
        "remedy": "Remove infected leaves, apply appropriate fungicides, maintain spacing."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "symptoms": "Curling leaves, stunted growth, yellowing leaf edges.",
        "remedy": "Remove infected plants, use virus-resistant varieties, control whiteflies."
    },
    "Tomato___Tomato_mosaic_virus": {
        "symptoms": "Mottled yellow/green leaves, distorted or stunted growth.",
        "remedy": "Disinfect tools, remove infected plants, avoid tobacco exposure near plants."
    },
    "Tomato___healthy": {
        "symptoms": "Green foliage, healthy stems and fruits, no spotting or curling.",
        "remedy": "Use well-drained soil, water consistently at base, monitor regularly."
    }
}