import streamlit as st

def get_best_friends(my_mbti):
    """
    내 MBTI에 따른 베프 MBTI 리스트를 반환합니다.
    이 데이터는 일반적인 MBTI 궁합 정보를 기반으로 합니다.
    """
    mbti_best_friends = {
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
    return mbti_best_friends.get(my_mbti.upper(), [])

st.set_page_config(
    page_title="MBTI 베프 찾기",
    page_icon="👯‍♀️",
    layout="centered"
)

st.title("👯‍♀️ MBTI 베프 찾기")
st.markdown("당신의 MBTI를 입력하고 최고의 친구 유형을 찾아보세요!")

# MBTI 선택 드롭다운
mbti_options = sorted([
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
])
my_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_options, index=None, placeholder="MBTI 선택...")

if my_mbti:
    st.subheader(f"당신의 MBTI는 **{my_mbti}** 이시군요!")
    best_friends = get_best_friends(my_mbti)

    if best_friends:
        st.success(f"**{my_mbti}** 님을 위한 최고의 베프 MBTI는 바로...")
        for bf_mbti in best_friends:
            st.markdown(f"### ✨ **{bf_mbti}**")
        st.markdown(
            "물론 MBTI 궁합은 재미로 보는 것이고, 어떤 MBTI 유형이든 좋은 친구가 될 수 있습니다! 😊"
        )
    else:
        st.warning("죄송합니다. 해당 MBTI에 대한 베프 정보를 찾을 수 없습니다.")

st.markdown("---")
st.caption("개발자: Gemini AI")
