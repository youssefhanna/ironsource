package intenium.rats {
  import flash.display.DisplayObject;
  import flash.display.MovieClip;
  import flash.display.StageAlign;
  import flash.display.StageScaleMode;
  import flash.events.Event;
  import flash.events.IOErrorEvent;
  import flash.events.ProgressEvent;
  import flash.geom.Point;
  import flash.utils.getDefinitionByName;


  /**
   * Waits for whole program to be loaded displaying loading screen and then launches program's enty point.
   * @author ilych
   */
  [SWF(width="960", height="640", frameRate = "24", backgroundColor = "#000000")]
  public class Client extends MovieClip {
    // -----------------------------------------------------------------------------
    // -----------------------------------------------------------------------------
    public function Client() {
 
 
    }
    // -----------------------------------------------------------------------------
    private function ioError( e : IOErrorEvent ) : void {
    }
    // -----------------------------------------------------------------------------
    private function progress( e : ProgressEvent ) : void {
  
    }
    // -----------------------------------------------------------------------------
    private function checkFrame( e : Event ) : void {

    }
    // -----------------------------------------------------------------------------
    private function loadingFinished() : void {

    }
    // -----------------------------------------------------------------------------
    private function startup() : void {
    
    }
    // -----------------------------------------------------------------------------
  }
}