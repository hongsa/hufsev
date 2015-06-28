/* 서버쪽으로 데이터를 보내보자 */
$(document).ready(function(){
    $('#actor_comment').click(function(){
        /* 일단 처리할 정보를 가져오자. ( jquery 이용 ) */
        var inputComment = $('input[name=comment]').val();
        var inputActorName = $('input[name=actorname]').val();

        if ((inputComment=="")|| inputComment==null){
            alert("내용을 입력해주세요!");
            return;
        }

        if ((inputComment.indexOf("<")!=-1) ||(inputComment.indexOf(">")!=-1) || (inputComment.indexOf("$")!=-1)
            ||(inputComment.indexOf("{")!=-1)||(inputComment.indexOf("}")!=-1)
            ||(inputComment.indexOf("[")!=-1)||(inputComment.indexOf("]")!=-1)||(inputComment.indexOf("/")!=-1))
        {
            alert("특수문자는 사용할 수 없습니다!");

            return;
        }

        $('input[type="text"],textarea').val('');
        var $target = $('html,body');
        $target.animate({scrollTop: $(document).height()-$(window).height()}, 300);

        /* 보낼 데이터 객체로 준비 ( 이게 제일 심플함. )
         서버에서는 input 이라는 이름으로 데이터를 받기로 약속되어져있다. AjaxSample.py 참고 */
        var sParam = {
            comment: inputComment,
            actorName: inputActorName
        }
        /* 보내보자 시바 */
        $.ajax({
            url: '/actor/comment', // 데이터 보낼 주소.
            data: sParam, // 데이터 보낼것 ( key = value 쌍 구조를 이루고있어야됨 )
            dataType: "JSON",
            method: 'POST', // 포스트로 보내기로했지?
            success: receiverHandler, // 핸들러 등록 아래 참고.
            error: errorHandler //
        });
    });
    $('#actor_input').keypress(function(e){
        if(e.which == 13){
            $('#actor_comment').click();
        }
    });
});
/* 서버에서 계산한 결과가 왔을때 처리할 부분 */
var receiverHandler = function(result, textStatus, xhr) {
    $
    /**
     * !! Notice !!
     * result 부분으로 서버에서 계산후 뿌려주는 json 형태의 (스트링) 이 들어오게된다.
     result = {
                data : 10
             }
     이런식으로 들어올거임. ( 하지만 문자열 이니깐 자바스크립트 객체로 변환할 작업이 필요하다 )
     textStatus, xhr 은 아직 당장은 필요없으니깐 재끼자.
     */
        //if( typeof result !== 'string')
        //
        //    return alert(result['comments']);
        //객체화 해보자.
        //var myData = JSON.parse(result);
        //alert(myData);
        //뷰에 뿌리자.
    $('#current').before('<div class="panel panel-default">'+'<div class="row">'+'<div class="col-sm-2 text-left">'+'<p class="comment_author">'+'<img src="/static/img/'+result['level']+'.png"/>'+'&nbsp;&nbsp;'+result['user']+'</p>'+'</div>'+'<div class="col-sm-9">'+'<p class="text-center commentBox">' +result['comments']+'</p>'+'</div>'+'</div>'+'</div>');
    //actorName을 뿌릴 땐 (myData.actorName) 이용
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-center",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "1500",
        "extendedTimeOut": "1500",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };

    Command: toastr["success"]("소중한 한줄평 저장완료되었습니다!");
}

var errorHandler = function(){
    alert('error')
}