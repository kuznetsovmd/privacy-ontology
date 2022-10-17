/*|1.93.2.95-S-95|publish|2022-06-14T14:48:16.765Z|*/
!function(t){t.version=t.version||"1.93.2.95-S-95",t.time=t.time||new Date(1655218096765)}(window["~hpe~"]||(window["~hpe~"]={})),(window["~hpeWpJsonp~"]=window["~hpeWpJsonp~"]||[]).push([[6],{"core/helpers/metrics-my-account":function(t,e,n){"use strict";n.r(e),n.d(e,"MetricsMyAccount",function(){return a});function o(t){return t.replace(".html","").split("/").slice(3).join(":")||""}var r=n("core/helpers/metrics"),e=n(24),i=n.n(e),c=function(){return(c=Object.assign||function(t){for(var e,n=1,o=arguments.length;n<o;n++)for(var r in e=arguments[n])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t}).apply(this,arguments)},a=(s.trackCreateAccountStart=function(t){void 0===t&&(t=s.getParentPageForCreateAccount),Object(r.trackMetrics)(s.hvaCreateAccountStart,{parentPage:t()})},s.trackCreateAccountComplete=function(t,e){void 0===t&&(t=s.getParentPageForCreateAccount),Object(r.trackMetrics)(s.hvaCreateAccountComplete,{parentPage:t(),emid:e})},s.trackSignInSuccess=function(t,e,n){void 0===n&&(n=!1),s.islockedSignInSuccessMutex()||(Object(r.trackMetrics)(s.hvaSignInSuccess,{parentPage:s.getParentPageForSignInSuccess(e,n),emid:t}),s.lockSignInSuccessMutex())},s.trackSignInFailure=function(){Object(r.trackMetrics)(s.hvaSignInFailure,{parentPage:s.getParentPageFromCurrent()})},s.fireLoginStartEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:c({page_name:"login:modal"},t&&{emid:t})}))},s.fireLoginSuccessEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"login:modal:success",emid:t}}))},s.fireLoginFailEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"login:modal:fail",emid:t}}))},s.fireCreateAccountStartEvent=function(){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"create-account:modal:start"}}))},s.fireCreateAccountCompleteEvent=function(t){window.dispatchEvent(new CustomEvent(s.eventMetrics,{detail:{page_name:"create-account:modal:complete",emid:t}}))},s.islockedSignInSuccessMutex=function(){return"1"===i.a.get(s.hvaSignInSuccess)},s.lockSignInSuccessMutex=function(){i.a.set(s.hvaSignInSuccess,"1")},s.unlockSignInSuccessMutex=function(){i.a.set(s.hvaSignInSuccess,"0")},s.getParentPageFromCurrent=function(){return o(window.location.pathname)},s.getParentPageFromReferer=function(){return o(new URL(document.referrer).pathname)},s.getParentPageForCreateAccount=function(){if(document.referrer){var t=new URLSearchParams(window.location.search);if(t.has("redirectURL"))return t.get("redirectURL");if(!t.has("resource")&&Object(r.isReferrerMatch)())return s.getParentPageFromReferer()}return"no-parent-page"},s.getParentPageForSignInSuccess=function(t,e){if(t.includes("passport")){t="no-parent-page";return e?t=s.getParentPageFromCurrent():document.referrer&&(t=Object(r.isReferrerMatch)()?s.getParentPageFromReferer():s.getParentPageFromCurrent()),t}return s.getParentPageFromCurrent()},s.hvaCreateAccountStart="hva.createaccount.start",s.hvaCreateAccountComplete="hva.createaccount.complete",s.hvaSignInSuccess="hva.sign-in.success",s.hvaSignInFailure="hva.sign-in.failure",s.eventMetrics="ANALYTICS.PAGEVIEW",s);function s(){}},"hpe-forms/services/marketo/lead":function(t,e,n){"use strict";n.d(e,"a",function(){return a});var o=n("core/helpers/promise-utils"),r=n(6),i=function(t,c,a,s){return new(a=a||Promise)(function(n,e){function o(t){try{i(s.next(t))}catch(t){e(t)}}function r(t){try{i(s.throw(t))}catch(t){e(t)}}function i(t){var e;t.done?n(t.value):((e=t.value)instanceof a?e:new a(function(t){t(e)})).then(o,r)}i((s=s.apply(t,c||[])).next())})},c=function(n,o){var r,i,c,a={label:0,sent:function(){if(1&c[0])throw c[1];return c[1]},trys:[],ops:[]},t={next:e(0),throw:e(1),return:e(2)};return"function"==typeof Symbol&&(t[Symbol.iterator]=function(){return this}),t;function e(e){return function(t){return function(e){if(r)throw new TypeError("Generator is already executing.");for(;a;)try{if(r=1,i&&(c=2&e[0]?i.return:e[0]?i.throw||((c=i.return)&&c.call(i),0):i.next)&&!(c=c.call(i,e[1])).done)return c;switch(i=0,c&&(e=[2&e[0],c.value]),e[0]){case 0:case 1:c=e;break;case 4:return a.label++,{value:e[1],done:!1};case 5:a.label++,i=e[1],e=[0];continue;case 7:e=a.ops.pop(),a.trys.pop();continue;default:if(!(c=0<(c=a.trys).length&&c[c.length-1])&&(6===e[0]||2===e[0])){a=0;continue}if(3===e[0]&&(!c||e[1]>c[0]&&e[1]<c[3])){a.label=e[1];break}if(6===e[0]&&a.label<c[1]){a.label=c[1],c=e;break}if(c&&a.label<c[2]){a.label=c[2],a.ops.push(e);break}c[2]&&a.ops.pop(),a.trys.pop();continue}e=o.call(n,a)}catch(t){e=[6,t],i=0}finally{r=c=0}if(5&e[0])throw e[1];return{value:e[0]?e[1]:void 0,done:!0}}([e,t])}}},a=(s.buildURL=function(t){var e=t.url,n=t.email,t=t.fields;return Object(r.b)(e||s.DEFAULT_LEAD_URL,{leadEmail:encodeURIComponent(n),fieldsList:t.join()})},s.load=function(n){return i(this,void 0,Promise,function(){var e;return c(this,function(t){switch(t.label){case 0:return e=s.buildURL(n),[4,fetch(e)];case 1:return e=t.sent(),[4,o.default.fetchJson(e)];case 2:return[2,t.sent()]}})})},s.DEFAULT_LEAD_URL="/services/hpe/marketo/prefill?leadEmail={leadEmail}&fieldsList={fieldsList}",s);function s(){}},"hpe-my-account/abstract-service":function(t,e,n){"use strict";n.d(e,"a",function(){return o});var o=function(t){this.formName=t.formName,this.mode=t.mode||"default"}},"hpe-my-account/account-creation-v2":function(t,e,n){"use strict";n.r(e),n.d(e,"COUNTRY_FIELD_NAME",function(){return P});var o,r,i=n("core/log"),c=n("core/view"),a=n("core/helpers/dom"),s=n(0),u=n(2),l=n("core/helpers/config"),p=n("core/helpers/scroll"),f=n("core/helpers/auth-api"),h=n("core/helpers/metrics-my-account"),d=n("cockpit/api/shared"),m=n("demandgen/utils/checkboxes-preselection"),b=n("hpe-forms/hpe-form-item"),y=n("hpe-forms/hpe-form-wrapper"),v=n("hpe-my-account/init-service"),g=n(27),S=(o=function(t,e){return(o=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function n(){this.constructor=t}o(t,e),t.prototype=null===e?Object.create(e):(n.prototype=e.prototype,new n)}),w=function(){return(w=Object.assign||function(t){for(var e,n=1,o=arguments.length;n<o;n++)for(var r in e=arguments[n])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t}).apply(this,arguments)},n=function(t,e,n,o){var r,i=arguments.length,c=i<3?e:null===o?o=Object.getOwnPropertyDescriptor(e,n):o;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)c=Reflect.decorate(t,e,n,o);else for(var a=t.length-1;0<=a;a--)(r=t[a])&&(c=(i<3?r(c):3<i?r(e,n,c):r(e,n))||c);return 3<i&&c&&Object.defineProperty(e,n,c),c},C="ACCOUNT_CREATION_V2",P="residentCountryCode",s=(r=c.default,S(O,r),O.prototype.init=function(){var e=this;b.HPEFormItem.register(),y.HPEFormWrapper.register(),this._apiReady=d.SharedAPI.cockpit$.then(function(t){return e._api=t}),this._fireCreateAccStartDebounced=Object(g.debounce)(function(){h.MetricsMyAccount.fireCreateAccountStartEvent()},100),this.checkboxesPreselection=new m.CheckboxesPreselection({form:this.$form,checkboxesSelector:"input[type='checkbox']",countryFieldSelector:"select[name='".concat(P,"']")}),this.toFormState(),this._fireCreateAccStartDebounced()},Object.defineProperty(O.prototype,"thirdPartyService",{get:function(){return Object(v.a)(this.options.thirdPartyService,{formName:this.options.thirdPartyServiceFormId})},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"$formState",{get:function(){return this.find(this.options.formState)},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"$submitState",{get:function(){return this.find(this.options.submitState)},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"$blockedState",{get:function(){return this.find(this.options.blockedState)},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"$form",{get:function(){return Object(a.unwrap)(this.find(this.options.form))},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"preferredLanguage",{get:function(){var t=Object(l.getConfig)("i18n.lc");return"ar"===t?"en":t},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"acceptanceNotification",{get:function(){return this.find(this.options.acceptanceNotification)},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"submitNotification",{get:function(){return this.find(this.options.submitNotification)},enumerable:!1,configurable:!0}),Object.defineProperty(O.prototype,"$submit",{get:function(){return $(this.$form).find(this.options.submit)},enumerable:!1,configurable:!0}),O.prototype["{form} input,select,button[type='submit'] on:focus click"]=function(){this._onCreateAccountStart()},O.prototype["{form} on:hpe:form:submit"]=function(){this._submitForm()},O.prototype["{body} .modal on:shown.bs.modal"]=function(){this.toFormState()},O.prototype["on:modal-content:open"]=function(){this._fireCreateAccStartDebounced()},O.prototype._prepareData=function(t){var e=this.$form.serialize();return"passport"===t&&this.options.skipFieldsInPassportSubmit.forEach(function(t){delete e[t]}),"marketo"===t&&Object.keys(e).forEach(function(t){""===e[t]&&delete e[t]}),w(w({},e),{preferredLanguage:this.preferredLanguage})},O.prototype._onCreateAccountStart=function(){h.MetricsMyAccount.trackCreateAccountStart(h.MetricsMyAccount.getParentPageFromCurrent)},O.prototype._submitForm=function(){var e=this;this._hideNotify(),this._showSpinner();var t=this._prepareData("passport");this._apiReady.then(function(){return e._checkUserExist(t)}).then(function(){return e.thirdPartyService.submitData(e._prepareData(e.options.thirdPartyService))}).then(function(){return e._createAccount(t)}).catch(function(t){t&&(Object(i.error)(t),"RplCheckFailedException"===t.code?e.toBlockedState():e._showSubmitNotify(e.options.errMsg)),e._hideSpinner()})},O.prototype._checkUserExist=function(t){var e=this;return this._api.auth.isUserExist(t.emailAddress).catch(function(){return Promise.resolve({})}).then(function(t){return!t.status||t.providers&&-1===t.providers.indexOf("passport")?Promise.resolve():(Object(i.debug)("".concat(C,": checkUser response"),t),e._showSubmitNotify(e.options.emailExistsErrMsg),Promise.reject())})},O.prototype._createAccount=function(e){var n=this;return this._api.auth.createAccount("passport",e).then(function(t){if(t.exception)n._showSubmitNotify(f.AUTH_API_ERROR_PROCESSOR.getExceptionMsg(t));else if(Object(i.debug)("".concat(C,": create account response"),t),n._isValidCreateAccountResponse(t,e)){n.toSubmitState(),h.MetricsMyAccount.fireCreateAccountCompleteEvent(t.emailAddress);try{h.MetricsMyAccount.trackCreateAccountComplete(h.MetricsMyAccount.getParentPageFromCurrent,t.emailAddress)}catch(t){Object(i.debug)("".concat(C,": metric error: "),t)}n.$form.reset(),n._hideSpinner()}else n.toErrorState()})},O.prototype.toFormState=function(){this.$formState.removeClass(this.options.hiddenClass),this.$submitState.addClass(this.options.hiddenClass),this.$blockedState.addClass(this.options.hiddenClass)},O.prototype.toErrorState=function(){this._showSubmitNotify(this.options.errMsg),Object(i.error)("Invalid create account response"),this._hideSpinner()},O.prototype.toSubmitState=function(){this.$formState.addClass(this.options.hiddenClass),this.$submitState.removeClass(this.options.hiddenClass),Object(p.scrollToTop)()},O.prototype.toBlockedState=function(){this.$formState.addClass(this.options.hiddenClass),this.$blockedState.removeClass(this.options.hiddenClass),Object(p.scrollToTop)()},O.prototype._showSpinner=function(){this.$submit.addClass(this.options.spinnerClass)},O.prototype._hideSpinner=function(){this.$submit.removeClass(this.options.spinnerClass)},O.prototype._hideNotify=function(){this.submitNotification.removeClass(this.options.showNotificationClass)},O.prototype._showSubmitNotify=function(t){this.submitNotification.text(t),this.submitNotification.addClass(this.options.showNotificationClass)},O.prototype.onDestroy=function(){this.checkboxesPreselection.unbindEvents(),r.prototype.onDestroy.call(this)},O.prototype._isValidCreateAccountResponse=function(t,e){return t.userId&&t.emailAddress&&t.userId===t.emailAddress&&t.emailAddress===e.emailAddress},O.defaults={formState:".ac-v2-form-state",submitState:".ac-v2-submit-state",blockedState:".ac-v2-blocked-state",form:".js-ac-v2-form-wrapper",submitNotification:".js-submit-notification",submit:".submit-btn",showNotificationClass:"visible",hiddenClass:"hidden",spinnerClass:"spinner-shown",skipFieldsInPassportSubmit:["emailOptIn","phoneOptIn"]},n([Object(u.a)()],O.prototype,"thirdPartyService",null),n([Object(u.a)()],O.prototype,"$formState",null),n([Object(u.a)()],O.prototype,"$submitState",null),n([Object(u.a)()],O.prototype,"$blockedState",null),n([Object(u.a)()],O.prototype,"$form",null),n([Object(u.a)()],O.prototype,"preferredLanguage",null),n([Object(u.a)()],O.prototype,"acceptanceNotification",null),n([Object(u.a)()],O.prototype,"submitNotification",null),n([Object(u.a)()],O.prototype,"$submit",null),n([Object(u.a)()],O.prototype,"_onCreateAccountStart",null),n([s.a],O.prototype,"toErrorState",null),O);function O(){return null!==r&&r.apply(this,arguments)||this}e.default=s},"hpe-my-account/eloqua-service":function(t,e,n){"use strict";n.d(e,"a",function(){return v});var o,r=n("core/helpers/promise-utils"),u=n("core/helpers/config"),i=n("core/helpers/cache"),s=n(50),l=n(19),p=n("core/log"),f=n("hpe-forms/form-cookies"),e=n("hpe-my-account/abstract-service"),n=(o=function(t,e){return(o=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function n(){this.constructor=t}o(t,e),t.prototype=null===e?Object.create(e):(n.prototype=e.prototype,new n)}),c=function(){return(c=Object.assign||function(t){for(var e,n=1,o=arguments.length;n<o;n++)for(var r in e=arguments[n])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t}).apply(this,arguments)},h=function(t,c,a,s){return new(a=a||Promise)(function(n,e){function o(t){try{i(s.next(t))}catch(t){e(t)}}function r(t){try{i(s.throw(t))}catch(t){e(t)}}function i(t){var e;t.done?n(t.value):((e=t.value)instanceof a?e:new a(function(t){t(e)})).then(o,r)}i((s=s.apply(t,c||[])).next())})},d=function(n,o){var r,i,c,a={label:0,sent:function(){if(1&c[0])throw c[1];return c[1]},trys:[],ops:[]},t={next:e(0),throw:e(1),return:e(2)};return"function"==typeof Symbol&&(t[Symbol.iterator]=function(){return this}),t;function e(e){return function(t){return function(e){if(r)throw new TypeError("Generator is already executing.");for(;a;)try{if(r=1,i&&(c=2&e[0]?i.return:e[0]?i.throw||((c=i.return)&&c.call(i),0):i.next)&&!(c=c.call(i,e[1])).done)return c;switch(i=0,c&&(e=[2&e[0],c.value]),e[0]){case 0:case 1:c=e;break;case 4:return a.label++,{value:e[1],done:!1};case 5:a.label++,i=e[1],e=[0];continue;case 7:e=a.ops.pop(),a.trys.pop();continue;default:if(!(c=0<(c=a.trys).length&&c[c.length-1])&&(6===e[0]||2===e[0])){a=0;continue}if(3===e[0]&&(!c||e[1]>c[0]&&e[1]<c[3])){a.label=e[1];break}if(6===e[0]&&a.label<c[1]){a.label=c[1],c=e;break}if(c&&a.label<c[2]){a.label=c[2],a.ops.push(e);break}c[2]&&a.ops.pop(),a.trys.pop();continue}e=o.call(n,a)}catch(t){e=[6,t],i=0}finally{r=c=0}if(5&e[0])throw e[1];return{value:e[0]?e[1]:void 0,done:!0}}([e,t])}}},m=function(t){var e="function"==typeof Symbol&&Symbol.iterator,n=e&&t[e],o=0;if(n)return n.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&o>=t.length&&(t=void 0),{value:t&&t[o++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")},b=function(t,e){var n="function"==typeof Symbol&&t[Symbol.iterator];if(!n)return t;var o,r,i=n.call(t),c=[];try{for(;(void 0===e||0<e--)&&!(o=i.next()).done;)c.push(o.value)}catch(t){r={error:t}}finally{try{o&&!o.done&&(n=i.return)&&n.call(i)}finally{if(r)throw r.error}}return c},a=new i.Cache({ns:"eloqua-account",long:!0,liveTime:1440});var y,v=(y=e.a,n(g,y),g.prototype.getLeadFields=function(c,a){return h(this,void 0,Promise,function(){var e,n,o,r,i=this;return d(this,function(t){switch(t.label){case 0:return[4,this.loadConfigs()];case 1:t.sent(),e=3,n=0,t.label=2;case 2:return!o&&n<e?[4,function(o){return h(this,void 0,Promise,function(){var e,n;return d(this,function(t){switch(t.label){case 0:return e=decodeURIComponent("<C_EmailAddress>".concat(o,"</C_EmailAddress>")),n=(new Date).getTime()+Object(l.randUID)(),[4,Object(s.loadScript)("eloqua-lookup-script-".concat(n),"".concat("https://etrack.ext.hpe.com","/visitor/v200/svrGP.aspx?pps=").concat("50","&siteid=").concat("2048","&DLKey=").concat("10831b2db3a34b9ea5863b752a46bfad","&DLLookup=").concat(e,"&ms=").concat("193","&_=").concat(n))];case 1:return t.sent(),[2,window.GetElqContentPersonalizationValue]}})})}(c)]:[3,4];case 3:return o=t.sent(),n++,[3,2];case 4:if(o)return r={},a.forEach(function(t){r[t]=o(t)}),Object.keys(r).forEach(function(e){var t=null===(t=document.querySelector('[data-eloqua-name="'.concat(e,'"]')))||void 0===t?void 0:t.getAttribute("name");t&&i.configs[t]&&i.configs[t].forEach(function(t){t.fullName===r[e]&&(r[e]=t.passportCode)})}),[2,{status:"success",data:r}];throw Error("Error while fetching eloqua data")}})})},g.prototype.getLeadSubscriptions=function(r,i){return h(this,void 0,Promise,function(){var e,n,o=this;return d(this,function(t){switch(t.label){case 0:return[4,this.getLeadFields(r,[i])];case 1:return e=t.sent(),n={},[2,new Promise(function(t){(e.data[i]&&e.data[i].split("::")||[]).forEach(function(t){n[t]=!0}),t({status:"success",data:o.eloquaSubscriptionsList=n})})]}})})},g.prototype.buildUrl=function(t){return window["~hpe~"].root.replace("/js/",t)},g.prototype.formatValue=function(t,e){return Array.isArray(e)?e.join("::"):this.configs[t]?this.mapValueToEloqua(this.configs[t],e):e},g.prototype.mapValueToEloqua=function(t,e){t=t.find(function(t){return t.passportCode===e});return t?t.fullName:""},g.prototype.mapFieldsToEloqua=function(t){var e,n,o=new FormData;try{for(var r=m(Object.entries(t)),i=r.next();!i.done;i=r.next()){var c=b(i.value,2),a=c[0],s=c[1],c=null===(c=null===(c=this.configs.sectionSpecificFields)||void 0===c?void 0:c[this.mode])||void 0===c?void 0:c[a],c=c||this.configs.fields[a];c&&o.append(c,encodeURIComponent(this.formatValue(a,s)))}}catch(t){e={error:t}}finally{try{i&&!i.done&&(n=r.return)&&n.call(r)}finally{if(e)throw e.error}}if(o.append("elqSiteID",encodeURIComponent("2048")),o.append("elqCountryCode",encodeURIComponent(Object(u.pageLocaleValues)().country.toLowerCase())),o.append("elqLanguageCode",encodeURIComponent(Object(u.pageLocaleValues)().language.toLowerCase())),o.append("elqFormName",encodeURIComponent(this.formName)),o.append("elqOriginationPageUrl",encodeURIComponent(window.location.href)),Object(f.b)())try{o.append("mcid",window.s.visitor.getMarketingCloudVisitorID()),o.append("mcid_tid",(new Date).getTime().toString())}catch(t){Object(p.error)("Unable to retrieve mcid value - s.visitor.getMarketingCloudVisitorID is unavailable",t)}return o},g.prototype.submitSubscriptions=function(e){if(e.masterOptIn)return e.masterOptIn="N",this.submitData(e);var n={aprimoAssetIDMostRecent:"",emailAddress:""};Object.keys(n).forEach(function(t){n[t]=e[t],delete e[t]});var o="";return Object.keys(e).forEach(function(t){e[t]&&(o="".concat(o).concat(t,"::"))}),Object.keys(this.eloquaSubscriptionsList).forEach(function(t){Object.prototype.hasOwnProperty.call(e,t)||(o="".concat(o).concat(t,"::"))}),0<o.length&&(o=o.slice(0,-2)),this.submitData(c(c({},n),{subscriptions:o}))},g.prototype.submitData=function(e){return h(this,void 0,Promise,function(){return d(this,function(t){switch(t.label){case 0:return[4,this.loadConfigs()];case 1:return t.sent(),[2,fetch(g.eloquaSubmitPath,{method:"post",body:this.mapFieldsToEloqua(e)}).then(r.PromiseUtils.fetchText)]}})})},g.prototype.loadConfigs=function(){var o=this;return new Promise(function(e){var n=o.buildUrl(g.fieldsMappingUrl),t=a.get(n);t?(o.configs=t,e(o)):fetch(n).then(r.PromiseUtils.fetchJson).then(function(t){a.set(n,t),o.configs=t,e(o)})})},g.fieldsMappingUrl="/configs/eloqua-fields-mapping.json",g.eloquaSubmitPath="/services/hpe/eloqua.submit?disabledUserRecognition=true",g);function g(){return null!==y&&y.apply(this,arguments)||this}},"hpe-my-account/init-service":function(t,e,n){"use strict";n.d(e,"a",function(){return r});var e=n("hpe-my-account/eloqua-service"),n=n("hpe-my-account/marketo-service"),o={eloqua:e.a,marketo:n.a};function r(t,e){return new o[t](e)}},"hpe-my-account/marketo-service":function(t,e,n){"use strict";n.d(e,"a",function(){return u});var o,r,i=n("hpe-forms/services/marketo/lead"),c=n("hpe-forms/services/marketo/submit"),e=n("hpe-my-account/abstract-service"),n=(o=function(t,e){return(o=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function n(){this.constructor=t}o(t,e),t.prototype=null===e?Object.create(e):(n.prototype=e.prototype,new n)}),a=function(t,c,a,s){return new(a=a||Promise)(function(n,e){function o(t){try{i(s.next(t))}catch(t){e(t)}}function r(t){try{i(s.throw(t))}catch(t){e(t)}}function i(t){var e;t.done?n(t.value):((e=t.value)instanceof a?e:new a(function(t){t(e)})).then(o,r)}i((s=s.apply(t,c||[])).next())})},s=function(n,o){var r,i,c,a={label:0,sent:function(){if(1&c[0])throw c[1];return c[1]},trys:[],ops:[]},t={next:e(0),throw:e(1),return:e(2)};return"function"==typeof Symbol&&(t[Symbol.iterator]=function(){return this}),t;function e(e){return function(t){return function(e){if(r)throw new TypeError("Generator is already executing.");for(;a;)try{if(r=1,i&&(c=2&e[0]?i.return:e[0]?i.throw||((c=i.return)&&c.call(i),0):i.next)&&!(c=c.call(i,e[1])).done)return c;switch(i=0,c&&(e=[2&e[0],c.value]),e[0]){case 0:case 1:c=e;break;case 4:return a.label++,{value:e[1],done:!1};case 5:a.label++,i=e[1],e=[0];continue;case 7:e=a.ops.pop(),a.trys.pop();continue;default:if(!(c=0<(c=a.trys).length&&c[c.length-1])&&(6===e[0]||2===e[0])){a=0;continue}if(3===e[0]&&(!c||e[1]>c[0]&&e[1]<c[3])){a.label=e[1];break}if(6===e[0]&&a.label<c[1]){a.label=c[1],c=e;break}if(c&&a.label<c[2]){a.label=c[2],a.ops.push(e);break}c[2]&&a.ops.pop(),a.trys.pop();continue}e=o.call(n,a)}catch(t){e=[6,t],i=0}finally{r=c=0}if(5&e[0])throw e[1];return{value:e[0]?e[1]:void 0,done:!0}}([e,t])}}},u=(r=e.a,n(l,r),l.prototype.getLeadFields=function(e,n){return a(this,void 0,Promise,function(){return s(this,function(t){return[2,i.a.load({email:e,fields:n})]})})},l.prototype.getLeadSubscriptions=function(t,e){return this.getLeadFields(t,e.split(","))},l.prototype.prepareData=function(t){return t.formId=this.formName,t},l.prototype.submitSubscriptions=function(t){return this.submitData(t)},l.prototype.submitData=function(t){t=c.a.injectVisitorID(t);return c.a.submit({data:this.prepareData(t)})},l);function l(){return null!==r&&r.apply(this,arguments)||this}}}]);