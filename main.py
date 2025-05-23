import streamlit as st

def get_best_friends(my_mbti):
    """
    내 MBTI에 따른 베프 MBTI 리스트를 반환합니다.
    이 데이터는 일반적인 MBTI 궁합 정보를 기반으로 합니다.
    """
    mbti_best_friends_map = {
        "ISTJ": ["ESFP", "ESTP"],
        "ISFJ": ["ESFP", "ESTP"],
        "INFJ": ["ENFP", "ENTP"],
        "INTJ": ["ENFP", "ENTP"],
        "ISTP": ["ESFJ", "ESTJ"],
        "ISFP": ["ENFJ", "ESFJ"],
        "INFP": ["ENFJ", "ENTJ"],
        "INTP": ["ENTJ", "ESTJ"],
        "ESTP": ["ISFJ", "ISTJ"],
        "ESFP": ["ISFJ", "ISTJ"],
        "ENFP": ["INFJ", "INTJ"],
        "ENTP": ["INFJ", "INTJ"],
        "ESTJ": ["INTP", "ISTP"],
        "ESFJ": ["INFP", "ISTP"],
        "ENFJ": ["INFP", "ISFP"],
        "ENTJ": ["INTP", "INFP"],
    }
    # 대소문자 구분 없이 처리하기 위해 입력값을 대문자로 변환
    return mbti_best_friends_map.get(my_mbti.upper(), [])

st.set_page_config(
    page_title="MBTI 베프 찾기 앱",
    page_icon="👯‍♀️",
    layout="centered"
)

st.title("💖 MBTI 베프 찾기")
st.markdown("당신의 MBTI를 선택하고, 나와 잘 맞는 베프 유형을 찾아보세요!")

# MBTI 선택 드롭다운
mbti_options = sorted([
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
])
# placeholder 옵션을 사용하여 초기 안내 텍스트를 표시
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_options, index=None, placeholder="👇 MBTI를 선택하세요...")

if selected_mbti:
    st.markdown(f"## 당신의 MBTI는 **{selected_mbti}** 이시군요!")
    best_friends = get_best_friends(selected_mbti)

    if best_friends:
        st.success(f"**{selected_mbti}** 님과 찰떡궁합인 베프 MBTI 유형은 바로...")
        for bf_mbti in best_friends:
            st.markdown(f"### ✨ **{bf_mbti}**")
        st.markdown(
            "---"
            "⚠️ **주의**: MBTI 궁합은 재미로 보는 것이며, 모든 유형의 친구들과 좋은 관계를 맺을 수 있습니다! 😊"
        )
    else:
        st.warning("죄송합니다. 선택하신 MBTI에 대한 베프 정보를 찾을 수 없습니다. (데이터 부족)")

st.markdown("---")
st.caption("개발자: Gemini AI")
