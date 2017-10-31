<template>
  <div class="choose">
    <div class="choose-son">
      属性方式：
      <el-input class="ele-input"
        placeholder="请选择日期"
        suffix-icon="el-icon-date"
        v-model="input2">
      </el-input>
    </div>
    <div class="choose-son">
      属性方式：
      <el-input class="ele-input"
                placeholder="请选择日期"
                suffix-icon="el-icon-date"
                v-model="input2">
      </el-input>
    </div>
    <div class="choose-son">
      属性方式：
      <el-input class="ele-input"
                placeholder="请选择日期"
                suffix-icon="el-icon-date"
                v-model="input2">
      </el-input>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  export default{

  };
</script>
<style lang="stylus" rel="stylesheet/stylus">
  .choose
    width: 240px
    height: 200px
    position: absolute
    right:15px
    top:50px
    .choose-son
      width: 230px
      height: 50px
      margin: 12px
      background: #787878
      opacity: 0.5
      color:white
      padding: 5px
      .ele-input
        width:140px
        line-height: 50px
</style>
