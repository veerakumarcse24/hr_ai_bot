import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
@Injectable()
export class ChatService {

  constructor(private http:HttpClient) { }

  converse(chatmsg) {
    return this.http.get(environment.hrBackend + `chat?inputmsg=`+chatmsg).toPromise();
  }

}
