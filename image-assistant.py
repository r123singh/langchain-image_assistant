
from utils import(
    desc_image_chain,
    chart_analysis_chain,
    damage_assess_chain,
    product_analyzer_chain,
    initialize_agent_executor,
    get_llm_instance,
    encode_image
)

llm = get_llm_instance()

image_chain = desc_image_chain(llm)
chart_chain = chart_analysis_chain(llm)
damage_chain = damage_assess_chain(llm)
product_chain = product_analyzer_chain(llm)

agent_executor = initialize_agent_executor()

def simple_image_description():
    image_url = input("Enter the Image URL: ")
    category = input("Enter the image category/type(eg. wildlife, nature, cartoon, landscape etc.): ")
    response = input("Enter tone in which response is generated(hilarious, happy, thrilling): ")
    result = image_chain.run(image_cat = category, image_url = image_url, response_type = response)
    return result
    
def graphs_chart_analyzer():
    image_url = input("Enter the chart or graph based Image URL: ")
    result = chart_chain.run(chart_image_url = image_url)
    return result
    
def vehicle_damage_analysis():
    car_before_image = input("Enter the image URL of the car before accident: ")
    car_after_image = input("Enter the image URL of the car after accident: ")
    result = damage_chain.run(car_image_before_url = car_before_image, car_image_after_url = car_after_image)
    return result
    
def product_image_analysis():
    product_image = input("Enter the image URL of the product to scan: ")
    result = product_chain.run(product_image_url = product_image)
    return result
    
def main():
    
    keepRunning = True
    while keepRunning:
        print("*******************************************************")
        print("******************OPENAI IMAGE ASSISTANT***************")
        print("*******************************************************")
        print("1. Analyze images to generate response in different tones")
        print("2. Explain graphical Charts and generate Desriptive analysis")
        print("3. Insurance image assistant for Vehicle Damage assessment")
        print("4. Scan Product images and Output Products Descriptions")
        print("5. Exit")

        choice = input("Enter Choice: ") 
        
        if choice == '1':
            description = simple_image_description()
            print("Image description: ")
            print(description)
        elif choice == '2':
            analysis = graphs_chart_analyzer()
            print("Chart Analysis: ")
            print(analysis)
        elif choice == '3':
            assessment = vehicle_damage_analysis()
            print("Insurance Assessment: ")
            print(assessment)
        elif choice == '4':
            extraction = product_image_analysis()
            print("Product Description: ")
            print(extraction)
        elif choice == '5':
            keepRunning = False
        else:
            print("Invalid Input")
    print("Thank you! have a nice day")
    

if __name__ == "__main__":
    main()
    