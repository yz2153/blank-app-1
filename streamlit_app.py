# import numpy as np
# import pandas as pd
import random
from itertools import combinations
import streamlit as st


# 設定頁面的標題與副標題(模式選擇)
st.title(":cup_with_straw: The Destined Pour")
st.header("Select the generator mode you want!")

# 重置三種關於模式的限制的st.session_state
if 'calories_customized' not in st.session_state:
    st.session_state['calories_customized'] = 'NO'
if 'price_customized' not in st.session_state:
    st.session_state['price_customized'] = 'NO'
if 'ingredient_customized' not in st.session_state:
    st.session_state['ingredient_customized'] = 'NO'

# 重置calories相關的st.session_state (slider/type)
if "calories_value" not in st.session_state:
    st.session_state['calories_value'] = 350
# 重置budget相關的st.session_state (slider/type)
if "budget_value" not in st.session_state:
    st.session_state['budget_value'] = 50

# 重置關於口味與配料的st.session_state
if 'selected_type' not in st.session_state: # 重置segmented_control
    st.session_state['selected_type'] = ["Topping", "Taste", "Texture"]
if 'add_topping' not in st.session_state:
    st.session_state['add_topping'] = ":rainbow[YES]"

if 'selected_topping' not in st.session_state:
    st.session_state['selected_topping'] = ["焙烏龍茶凍 Oolong Tea Jelly"]
if 'topping_number_max' not in st.session_state:
    st.session_state['topping_number_max'] = 1

if 'selected_taste' not in st.session_state:
    st.session_state['selected_taste'] = []   
if 'selected_texture' not in st.session_state: # 這個的選擇還沒有完成
    st.session_state['selected_texture'] = [] 

if 'random_texture' not in st.session_state: 
    st.session_state['random_texture'] = ""
if 'selected_texture_display' not in st.session_state: 
    st.session_state['selected_texture_display'] = []
if 'check_reminder_status' not in st.session_state: 
    st.session_state['check_reminder_status'] = ""

# 重置用來放模式選擇結果的list
mode_badge_list = []

# def用來處理calories功能的開關的function
def calories_on_change():
    st.session_state['calories_customized'] = st.session_state["calories_temp"]
    return None

# 設定calories mode的選擇區
option_calories = st.radio(
    ":one: Do you want to customize the “calories” of your drinks?",
    [":rainbow[YES]", "NO",],
    key="calories_temp",
    index=1,
    on_change=calories_on_change,
    horizontal=True,
)

# def用來處理price功能的開關的function
def price_on_change():
    st.session_state['price_customized'] = st.session_state["price_temp"]
    return None

# 設定price mode的選擇區
option_price = st.radio(
    ":two: Do you want to customize the “price” of your drinks?",
    [":rainbow[YES]", "NO",], 
    key="price_temp",   
    index=1,
    on_change=price_on_change,
    horizontal=True,
)

# def用來處理ingredient功能的開關的function
def ingredient_on_change():
    st.session_state['ingredient_customized'] = st.session_state["ingredient_temp"]
    return None

# 設定ingredient mode的選擇區
option_ingredient = st.radio(
    ":three: Do you want to customize the “ingredient” of your drinks?",
    [":rainbow[YES]", "NO",],  
    key="ingredient_temp",  
    index=1,
    on_change=ingredient_on_change,
    horizontal=True,
)


if st.session_state['calories_customized'] != 'NO':
    badge_calories = ':orange-badge[Calories]'
else:
        badge_calories = ''

if st.session_state['price_customized'] != 'NO':
    badge_price = ':green-badge[Price]'
else:
        badge_price = ''

if st.session_state['ingredient_customized'] != 'NO':
    badge_ingredient = ':blue-badge[Ingredient]'
else:
        badge_ingredient = ''


# 顯示目前選擇的模式
if option_calories == 'NO' and option_price == 'NO' and option_ingredient == 'NO':
    st.markdown("✔️ You selected: :violet-badge[Random generator]")
else: 
    st.markdown("✔️ You selected: " + badge_calories + badge_price + badge_ingredient)

st.divider()

# --- option_calories 的區塊 ---
def update_from_calories_slider():
    st.session_state["calories_value"] = st.session_state["calories_slider_value"]
def update_from_calories_number():
    st.session_state["calories_value"] = st.session_state["calories_number_value"]


if option_calories != 'NO':
    st.markdown("<p style='font-size:20px; color:DarkMagenta; font-weight:bold;'>1️⃣ Setting Target Calories for Your Drink</p>", unsafe_allow_html=True)
    
    col_calories_slider, col_calories_numberinput = st.columns([6, 1])

    with col_calories_slider:
        st.slider(
            "calories_slider",
            min_value=0,
            max_value=1000,
            key="calories_slider_value",
            value=st.session_state["calories_value"],
            on_change=update_from_calories_slider,
            label_visibility = "collapsed", 
        )

    with col_calories_numberinput:
        st.number_input(
            "calories_numberinput",
            min_value=0,
            max_value=1000,
            key="calories_number_value",
            value=st.session_state["calories_value"],
            on_change=update_from_calories_number,
            label_visibility = "collapsed",
        )

    calories_text = st.session_state["calories_value"]
    st.markdown(f"""
    Your target calorie count for your drink is <span style='color: SlateBlue; font-weight: bold;'>{calories_text}</span> calories.
    """, unsafe_allow_html=True)

    st.divider()
# --- option_calories 的區塊 ---

# --- option_price 的區塊 ---
def update_from_price_slider():
    st.session_state["budget_value"] = st.session_state["price_slider_value"]

def update_from_price_number():
    st.session_state["budget_value"] = st.session_state["price_number_value"]


if option_price != 'NO':
    st.markdown("<p style='font-size:20px; color:DarkMagenta; font-weight:bold;'>2️⃣ Setting Your Budget</p>", unsafe_allow_html=True)
    
    col_price_slider, col_price_numberinput = st.columns([6, 1])

    
    with col_price_slider:
        st.slider(
            "price_slider",
            min_value=0,
            max_value=1000,
            key="price_slider_value",
            value=st.session_state["budget_value"],
            on_change=update_from_price_slider,
            label_visibility = "collapsed", 
        )

    with col_price_numberinput:
        st.number_input(
            "price_numberinput",
            min_value=0,
            max_value=1000,
            key="price_number_value",
            value=st.session_state["budget_value"],
            on_change=update_from_price_number,
            label_visibility = "collapsed",
        )

    budget_text = st.session_state["budget_value"]
    st.markdown(f"""
    Your budget is <span style='color: SlateBlue; font-weight: bold;'>{budget_text}</span> dollars.
    """, unsafe_allow_html=True)

    st.divider()
# --- option_price 的區塊 ---

# --- option_ingredient 的區塊 ---
def update_customization_selection(): # 設定更新selected_type的ession_state
    st.session_state.selected_type = st.session_state.customized_selection
def update_whether_to_add_topping():
    st.session_state.whether_to_add_topping = st.session_state.add_topping

def update_topping_selection(): # 設定更新topping的session_state
    st.session_state.selected_topping = st.session_state.temp_topping_selection
def update_topping_number_max(): # 設定更新topping的session_state
    st.session_state.topping_number_max = st.session_state.temp_topping_number_max

def update_taste_selection(): # 設定更新taste的session_state
    st.session_state.selected_taste = st.session_state.temp_taste_selection
def update_texture_selection(): # 設定更新texture的session_state
    st.session_state.selected_texture = st.session_state.temp_texture_selection

def update_check_button():
    st.session_state.check_combination_status = True

if option_ingredient != 'NO': # 有時間可以把這個區塊中的小區塊都改成st.container()
    # 區域大標題
    st.markdown("<p style='margin-bottom: 0px; font-size:20px; color:DarkMagenta; font-weight:bold;'>3️⃣ Customize Your Ingredients</p>", unsafe_allow_html=True)    
    # 標題
    st.markdown("<p style='margin-bottom: 0px; font-size:16px; color:DarkMagenta; font-weight:bold;'>Select the type you want to customize.</p>", unsafe_allow_html=True)
   
   # 設定 選擇客製化ingredients的segmented_control
    type_customization = ["Topping", "Taste", "Texture"]
    selected_type = st.segmented_control(
        "Select the type you want to customize",
        type_customization,
        default=["Topping", "Taste", "Texture"],
        selection_mode="multi",
        key="customized_selection",
        on_change=update_customization_selection,
        label_visibility = "collapsed",
    )


# 加料 Topping
if option_ingredient != 'NO' and "Topping" in selected_type:
    st.markdown("<p style='margin-bottom: 0px; font-size:16px; color:DarkSlateBlue; font-weight:bold;'> ① Customize Your Topping</p>", unsafe_allow_html=True)
    
    # 選擇是否要加料 (False->0)
    st.markdown("<p margin-bottom: 0px; style='font-size:14px; color:DarkSlateBlue; font-weight:bold;'>Select whether you want to add topping to your drink or not.</p>", unsafe_allow_html=True)
    whether_to_add_topping = st.radio(
        "Select whether you want to add topping to your drink or not.",
        [":rainbow[YES]", "NO",],
        index=0,
        key="add_topping",
        on_change=update_whether_to_add_topping,
        horizontal=True,
        label_visibility="collapsed",
    )
    
    if whether_to_add_topping!="NO": # 如果使用者想要加topping
        # 選擇要添加的topping數量上限 (後面還要跟選擇出來的topping範圍判斷一次)
        st.markdown("<p margin-bottom: 0px; style='font-size:14px; color:DarkSlateBlue; font-weight:bold;'>Select the maximum number of topping you want (number between 1-5). </p>", unsafe_allow_html=True)
        st.markdown("<p style='margin-bottom: 0px; font-size:12px; color:DarkGray; font-weight:bold;'>◇ We will select a number from 1 to the number you have set as the number of toppings to add.</p>", unsafe_allow_html=True)
        st.markdown("<p style='margin-bottom: 4px; font-size:12px; color:DarkGray; font-weight:bold;'>◇ If you later select fewer than the number you have set, we will use the number of toppings you have selected as the maximum number of toppings to add.</p>", unsafe_allow_html=True)
        # ◇ We will select a number from 1 to the number you have set as the number of toppings to add.
        # ◇ If you later select fewer than the number you have set, we will use the number of toppings you have selected as the maximum number of toppings to add.
        
        topping_number_max = st.number_input(
            "Select the maximum number of topping you want",
            min_value=1,
            max_value=5,
            key="temp_topping_number_max",
            value=1,
            on_change=update_topping_number_max,
            label_visibility = "collapsed",
        )
        
        topping = ["檸檬 Lemon", "香橙 Orange", "甘蔗 Sugar cane", "春梅 Green Plum", "柚子 Yuzu/Pomelo", "珍珠 Golden Bubble/Pearl", "焙烏龍茶凍 Oolong Tea Jelly"]

        # 選擇想要放入generator的topping範圍
        st.markdown("<p margin-top: 2px; margin-bottom: 2px; style='font-size:14px; color:DarkSlateBlue; font-weight:bold;'>Select the type of topping you would like to add to your drink.</p>", unsafe_allow_html=True)
        selected_topping = st.pills(
            "Select the type of topping you would like to add to your drink", 
            topping, 
            default=["珍珠 Golden Bubble/Pearl"],
            selection_mode="multi",
            key="temp_topping_selection",
            label_visibility = "collapsed",
            )

        selected_topping_display = ""
        if len(selected_topping)>0:
            for i in range((len(selected_topping)-1)):
                selected_topping_display = selected_topping_display + str(selected_topping[i]) + ', '
            selected_topping_display = selected_topping_display + str(selected_topping[-1])
            st.markdown("➡️ Your selected topping: " + selected_topping_display + ".")        
        else:
            selected_topping_display = ""
    else:
        st.markdown("➡️ You want a drink without topping.")

    # 如果有要加料的話，隨機出真正要放入generator的topping數量 (topping_number)
    if whether_to_add_topping!="NO" and len(selected_topping)>0:
        # topping_number_max是前面的number_input中使用者自訂的topping上限 
        selected_topping_number = len(selected_topping) # 數出使用者選擇的topping有幾項

        if selected_topping_number >= topping_number_max:
            topping_number = topping_number_max
        else:
            topping_number = selected_topping_number
    
        random_topping_result = random.sample(selected_topping, random.randint(1,int(topping_number)))  

    else: # 如果沒有要加料的話，將topping_number設定成0 (目前已加上防呆?)
        topping_number = 0

    st.divider()


# 風味 taste 這個區塊要改成"一定要選至少一個選項"
if option_ingredient != 'NO' and "Taste" in selected_type:
    st.markdown("<p style='margin-bottom: 0px; font-size:16px; color:DarkSlateBlue; font-weight:bold;'> ② Select the taste of the drink you prefer (select at least one option)</p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-bottom: 4px; font-size:12px; color:DarkGray; font-weight:bold;'>◇ We will randomly select a taste of your selection to be used as a reference for the generator.</p>", unsafe_allow_html=True)

    taste = ["清爽回甘 Refreshing & Sweet Tea Flavor", "醇濃茶香 Mellow Tea Flavor", "酸 Sour", "甜 Sweet", "酸甜 Sweet & Sour", "奶香 Milky Flavor"]
    selected_taste = st.pills(
        "Select the taste of the drink you prefer", 
        taste, 
        selection_mode="multi",
        key="temp_taste_selection",
        label_visibility = "collapsed",
        )
    
    # display 所有使用者選擇的項目，實際上隨機從中選出一個給generator
    random_taste = ""
    selected_taste_display = ""

    if len(selected_taste)>0:
        random_taste = random.choice(selected_taste) # 從使用者選擇的一或多個項目中選出一個
        
        for i in range((len(selected_taste)-1)): # 設定顯示在頁面上的選項
            selected_taste_display = selected_taste_display + str(selected_taste[i]) + ', '
        selected_taste_display = selected_taste_display + str(selected_taste[-1])
        
        st.markdown("➡️ Your selected taste: " + selected_taste_display + ".")
    else:
        random_taste = ""
        selected_taste_display = ""
        st.markdown("➡️ You'll get random taste of drinks!")
    st.divider()

# 口感 Texture

if option_ingredient != 'NO' and "Texture" in selected_type:
    st.markdown("<p style='margin-bottom: 0px; font-size:16px; color:DarkSlateBlue; font-weight:bold;'> ③ Select the texture of the drink you prefer</p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-bottom: 0px; font-size:12px; color:DarkGray; font-weight:bold;'>◇ We will randomly select a texture of your selection to be used as a reference for the generator.</p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-bottom: 4px; font-size:12px; color:DarkGray; font-weight:bold;'>◇ If you want to get random texture drinks, turn off texture customization above.</p>", unsafe_allow_html=True)
    
    texture = ["果粒 Fruitiness", "濃厚 Thick", "嚼感 Chewiness",]
    selected_texture= st.pills(
        "Select the texture of the drink you prefer", 
        texture, 
        selection_mode="multi",
        key="temp_texture_selection", 
        label_visibility = "collapsed", 
        )

    with st.form('check_and_reminder_form', clear_on_submit=False, border=False,):
        with st.container(border=True,):
            # 定義隨機+檢查函式：選項前後不搭的話，跳warning         
            # 把random+check結合
            def random_texture_and_check(selected_topping, selected_texture): # 輸入selected_texture 跑這個function
                random_texture = ""
                selected_texture_list = []
                random_texture = random.choice(selected_texture) # 從使用者選擇的一或多個項目中選出一個
                selected_texture_display = ""
                invalid_texture = False
                selected_texture_list = list(selected_texture)

                if ("果粒 Fruitiness" in selected_texture_list):
                    if not whether_to_add_topping or not any(item in selected_topping for item in ["檸檬 Lemon", "香橙 Orange", "柚子 Yuzu/Pomelo"]):
                        invalid_texture = True
                
                if ("嚼感 Chewiness" in selected_texture_list):
                    if not whether_to_add_topping or not any(item in selected_topping for item in ["珍珠 Golden Bubble/Pearl", "焙烏龍茶凍 Oolong Tea Jelly",]):
                        invalid_texture = True
                
                # 無論有沒有跳出warning 都可以做random 有warning的話 後續不輸出即可
                for i in range((len(selected_texture)-1)): # 設定顯示在頁面上的選項
                    selected_texture_display = selected_texture_display + str(selected_texture[i]) + ', '
                selected_texture_display = selected_texture_display + str(selected_texture[-1])
                
                return random_texture, selected_texture_display, invalid_texture
            # ---

            col_check_button, col_check_reminder = st.columns([1, 2])

            with col_check_button:
                submitted = st.form_submit_button("🔍 Check! ")    

            # 按下按紐再執行判斷+random；display 所有使用者選擇的項目，實際上隨機從中選出一個給generator    
            if submitted:
                if len(selected_texture)==0: # 沒有選擇texture
                    random_texture = ""
                    selected_texture_display = ""
                    st.session_state['check_reminder_status'] = "success_0"
    
                if len(selected_texture)>0 and len(selected_texture)<3:
                        random_texture, selected_texture_display, invalid_texture = random_texture_and_check(
                            selected_topping=selected_topping, selected_texture=selected_texture
                            )
                        st.session_state['random_texture'] = random_texture
                        st.session_state['selected_texture_display'] = selected_texture_display
                        st.session_state['invalid_texture'] = invalid_texture

                        if st.session_state['invalid_texture']==True: # 如果檢查不通過(跳出warning) 顯示這則訊息
                            st.session_state['check_reminder_status'] = "error"
                        if st.session_state['invalid_texture']==False: # 如果texture檢查通過 (沒有發出warning) 列出使用者選擇的項目
                            st.session_state['check_reminder_status'] = "success_12"

                if len(selected_texture)==3:
                    random_texture, selected_texture_display, invalid_texture = random_texture_and_check(
                            selected_topping=selected_topping, selected_texture=selected_texture
                            )
                    st.session_state['random_texture'] = random_texture
                    st.session_state['selected_texture_display'] = selected_texture_display
                    st.session_state['invalid_texture'] = invalid_texture

                    if st.session_state['invalid_texture']==True: # 如果檢查不通過(跳出warning) 顯示這則訊息
                        st.session_state['check_reminder_status'] = "error"
                    if st.session_state['invalid_texture']==False: # 如果texture檢查通過 (沒有發出warning) 列出使用者選擇的項目
                        st.session_state['check_reminder_status'] = "success_3"
                    
            with col_check_reminder:
                if st.session_state['check_reminder_status']=="": # 還沒有按過check的時候顯示的字樣
                    st.markdown("👈 Please click the check button after the selection is complete.")
                if st.session_state['check_reminder_status'] in ["success_0", "success_12", "success_3", ]: # 如果texture檢查通過 (沒有發出warning) 顯示這則訊息
                    st.markdown("🆗 Pass! This combination can be used. ")
                if st.session_state['check_reminder_status']=="error": # 如果檢查不通過(跳出warning) 顯示這則訊息
                    st.markdown("🚨 Please ensure that your selection is valid. ")

            # 顯示在button下方
            st.markdown("<p style='margin-top: 0px; margin-bottom: 0px; font-size:12px; color:DarkGray; font-weight:bold;'>◇ Please make sure your customized combination is valid before generating. </p>", unsafe_allow_html=True)

        with st.container():

            if st.session_state['check_reminder_status']=="error":
                st.markdown(
                        """
                        <div style="border-left: 0.3rem solid red; padding: 1rem; background-color: #ffe6e6;">
                            <strong>⚠️ ERROR: </strong><br>
                            Please make sure your topping option is turned on and you have selected the topping for the corresponding texture!<br><br>
                            <u>Reminds:</u><br>
                            ◇ If you choose “果粒 Fruitiness” for your texture, you need to choose topping “檸檬 Lemon” or “香橙 Orange” or “柚子 Yuzu/Pomelo”;<br>
                            ◇ If you choose “嚼感 Chewiness” for your texture, you need to choose topping “珍珠 Golden Bubble/Pearl” or “焙烏龍茶凍 Oolong Tea Jelly”.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
            if st.session_state['check_reminder_status']=="success_0": # 如果texture檢查通過 (沒有發出warning) 顯示這則訊息
                st.markdown(
                    f"""
                    <div style="border-left: 0.3rem solid green; padding: 1rem; background-color: #e6ffe6; border-radius: 0.5rem;">
                        <strong>✅ SUCCESS:</strong><br><br>
                        ➡️ You'll get random texture of drinks!<br><br>
                        ◇ Everything looks good. Proceed to generate your drink!
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            if st.session_state['check_reminder_status']=="success_12": # 如果texture檢查通過 (沒有發出warning) 列出使用者選擇的項目
                selected_texture_display = st.session_state.get('selected_texture_display', '')
                st.markdown(
                    f"""
                    <div style="border-left: 0.3rem solid green; padding: 1rem; background-color: #e6ffe6; border-radius: 0.5rem;">
                        <strong>✅ SUCCESS:</strong><br><br>
                        ➡️ Your selected texture: <b>{selected_texture_display}</b>.<br><br>
                        ◇ Everything looks good. Proceed to generate your drink!
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                # st.success("➡️ Your selected texture: " + st.session_state.get('selected_texture_display', '') + ".")
            if st.session_state['check_reminder_status']=="success_3":
                st.markdown(
                    f"""
                    <div style="border-left: 0.3rem solid green; padding: 1rem; background-color: #e6ffe6; border-radius: 0.5rem;">
                        <strong>✅ SUCCESS:</strong><br><br>
                        ➡️ You'll get random texture of drinks!<br><br>
                        ◇ Everything looks good. Proceed to generate your drink!
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                # st.success("➡️ You'll get random texture of drinks!")
            # st.session_state['check_reminder_status'] = False # 還原check_reminder_status的session_state
        
    st.divider()

# ----- 客製化設定結束 -----

# 一些emoji：🎲 ✅ ✔️ ⚠️ 🚨 👈 💸 🔥 🌟 🔄 ➡️ 🆗

# ----- 接入功能code的必要轉換 -----

st.write(type(selected_taste))
st.write(type(selected_texture))
st.write(type(selected_topping))




# ----- 接入功能code的必要轉換 -----

